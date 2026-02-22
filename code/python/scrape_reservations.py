#!/usr/bin/env python3
"""
Scrape reservation dates from yoyaku.e-kanagawa.lg.jp/Miura
and update content/posts/home.md with the latest schedule.
"""

import re
import pathlib
from datetime import date, timedelta
from playwright.sync_api import sync_playwright

ENTRY_URL = "https://yoyaku.e-kanagawa.lg.jp/miura/web/"
RESERVATIONS_URL = "https://yoyaku.e-kanagawa.lg.jp/Miura/Web/Wg_YoyakukakuninTorikeshi.aspx"
USERNAME = "011080066"
PASSWORD = "EthanSean1234"

HOME_MD = pathlib.Path(__file__).parent.parent.parent / "content/posts/home.md"


def scrape_dates():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        def handle_route(route):
            request = route.request
            if request.method == "POST" and "h_DoubleLoginWarningFlg" in (request.post_data or ""):
                body = request.post_data.replace(
                    "h_DoubleLoginWarningFlg=false",
                    "h_DoubleLoginWarningFlg=true"
                )
                route.continue_(post_data=body)
            else:
                route.continue_()

        page.route("**/Wg_Login.aspx", handle_route)

        page.goto(ENTRY_URL, wait_until="networkidle", timeout=20000)
        page.click("input[name='rbtnLogin']")
        page.wait_for_load_state("networkidle")

        page.fill("input[name='txtID']", USERNAME)
        page.fill("input[name='txtPass']", PASSWORD)
        page.click("input[name='ucPCFooter$btnForward']")
        page.wait_for_load_state("networkidle")

        if "Login" in page.url or "login" in page.url.lower():
            browser.close()
            raise RuntimeError("Login failed — check credentials or account lock.")

        page.click("input[name='btnNormal']")
        page.wait_for_load_state("networkidle")
        page.click("input[name='rbtnKakunin']")
        page.wait_for_load_state("networkidle")

        content = page.content()
        browser.close()

    # Parse dates like 2026/3/1
    raw = re.findall(r"\d{4}/\d{1,2}/\d{1,2}", content)
    booked = set()
    for d in raw:
        y, m, day = d.split("/")
        booked.add(date(int(y), int(m), int(day)))
    return booked


def all_sundays(start, end):
    """Return all Sundays from start to end inclusive."""
    days = []
    d = start + timedelta(days=(6 - start.weekday()) % 7)  # first Sunday >= start
    while d <= end:
        days.append(d)
        d += timedelta(weeks=1)
    return days


def update_home_md(booked_dates):
    today = date.today()
    future_booked = {d for d in booked_dates if d > today}

    if not future_booked:
        print("No future booked dates found.")
        return

    first = min(future_booked)
    last = max(future_booked)

    # Build table rows: all Sundays in range, booked = 開催, others = おやすみ
    rows = []
    for sunday in all_sundays(first, last):
        status = "開催" if sunday in future_booked else "おやすみ"
        label = f"{sunday.year}年{sunday.month}月{sunday.day}日"
        rows.append(f"|{label}|{status}|")

    new_table = "|日にち|開催|\n|----|----|\n" + "\n".join(rows)

    text = HOME_MD.read_text(encoding="utf-8")

    # Replace existing table
    updated = re.sub(
        r"\|日にち\|開催\|.*?\n(?:\|.*?\n)*",
        new_table + "\n",
        text,
        flags=re.DOTALL
    )

    HOME_MD.write_text(updated, encoding="utf-8")
    print(f"Updated {HOME_MD} with {len(rows)} rows.")
    for row in rows:
        print(" ", row)


def main():
    print("Scraping reservation dates...")
    booked = scrape_dates()
    print(f"Found {len(booked)} booked dates: {sorted(booked)}")

    print("\nUpdating home.md...")
    update_home_md(booked)


if __name__ == "__main__":
    main()
