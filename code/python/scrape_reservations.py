#!/usr/bin/env python3
"""
Scrape reservation dates from yoyaku.e-kanagawa.lg.jp/Miura
"""

import re
from playwright.sync_api import sync_playwright

ENTRY_URL = "https://yoyaku.e-kanagawa.lg.jp/miura/web/"
RESERVATIONS_URL = "https://yoyaku.e-kanagawa.lg.jp/Miura/Web/Wg_YoyakukakuninTorikeshi.aspx"
USERNAME = "011080066"
PASSWORD = "EthanSean1234"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Intercept the auto-submitted double-login POST and flip the flag to True
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

        # Step 1: Initialize session
        page.goto(ENTRY_URL, wait_until="networkidle", timeout=20000)

        # Step 2: Go to login page
        page.click("input[name='rbtnLogin']")
        page.wait_for_load_state("networkidle")

        # Step 3: Fill credentials and submit
        page.fill("input[name='txtID']", USERNAME)
        page.fill("input[name='txtPass']", PASSWORD)
        page.click("input[name='ucPCFooter$btnForward']")
        page.wait_for_load_state("networkidle")

        print("After login:", page.url)

        if "Login" in page.url or "login" in page.url.lower():
            print("Login failed. Page:", page.inner_text("body")[:200])
            browser.close()
            return

        # Step 4: From ModeSelect → click メニュー → click 予約確認・取消
        page.click("input[name='btnNormal']")
        page.wait_for_load_state("networkidle")
        print("Menu page:", page.url)

        page.click("input[name='rbtnKakunin']")
        page.wait_for_load_state("networkidle")
        print("Reservations page:", page.url)

        content = page.content()
        body_text = page.inner_text("body")

        # Extract dates
        date_pattern = re.compile(r"\d{4}年\d{1,2}月\d{1,2}日|\d{4}/\d{1,2}/\d{1,2}")
        dates = date_pattern.findall(content)

        print("\n--- Reservation Dates ---")
        if dates:
            for d in sorted(set(dates)):
                print(" ", d)
        else:
            print("No dates found. Page text:")
            print(body_text[:3000])

        browser.close()


if __name__ == "__main__":
    main()
