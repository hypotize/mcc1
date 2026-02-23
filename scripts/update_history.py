#!/usr/bin/env python3
"""
Regenerate content/history/_index.md from git history of content/posts/home.md.
Run from the repo root.
"""

import subprocess
import re
import sys
from datetime import date
from collections import defaultdict

REPO_ROOT = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True
).stdout.strip()

HOME_MD = "content/posts/home.md"
HISTORY_MD = f"{REPO_ROOT}/content/history/_index.md"

# Pre-table 2022 sessions: first session was March 27, then every Sunday.
# The schedule table was introduced July 3, 2022. These are estimated.
PRE_TABLE_2022 = [
    date(2022, 3, 27),
    date(2022, 4, 3),  date(2022, 4, 10), date(2022, 4, 17), date(2022, 4, 24),
    date(2022, 5, 1),  date(2022, 5, 8),  date(2022, 5, 15), date(2022, 5, 22), date(2022, 5, 29),
    date(2022, 6, 5),  date(2022, 6, 12), date(2022, 6, 19), date(2022, 6, 26),
    date(2022, 7, 3),
]

YEAR_PATTERN    = re.compile(r'\|(\d{4})年(\d{1,2})月(\d{1,2})日\|開催\|')
NO_YEAR_PATTERN = re.compile(r'\|(\d{1,2})月(\d{1,2})日\|開催\|')


def infer_dates(month_day_list, commit_date):
    """Assign years to (month, day) pairs using the commit date as anchor."""
    result = []
    year = commit_date.year
    prev_month = None
    for month, day in month_day_list:
        if prev_month is not None and month < prev_month:
            year += 1
        prev_month = month
        try:
            result.append(date(year, month, day))
        except ValueError:
            pass
    return result


def extract_dates(content, commit_date):
    dates = set()
    for m in YEAR_PATTERN.finditer(content):
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        try:
            dates.add(date(y, mo, d))
        except ValueError:
            pass
    no_year = [(int(m.group(1)), int(m.group(2))) for m in NO_YEAR_PATTERN.finditer(content)]
    dates.update(infer_dates(no_year, commit_date))
    return dates


def get_all_session_dates():
    log = subprocess.run(
        ["git", "log", "--pretty=format:%H %ai", "--", HOME_MD],
        capture_output=True, text=True, cwd=REPO_ROOT
    ).stdout.strip()

    all_dates = set(PRE_TABLE_2022)

    for line in log.splitlines():
        if not line:
            continue
        parts = line.split()
        hash_ = parts[0]
        commit_date = date.fromisoformat(parts[1])
        content = subprocess.run(
            ["git", "show", f"{hash_}:{HOME_MD}"],
            capture_output=True, text=True, cwd=REPO_ROOT
        ).stdout
        if content:
            all_dates.update(extract_dates(content, commit_date))

    # Also read the working-tree version (staged or unsaved changes)
    try:
        with open(f"{REPO_ROOT}/{HOME_MD}", encoding="utf-8") as f:
            working = f.read()
        all_dates.update(extract_dates(working, date.today()))
    except FileNotFoundError:
        pass

    return all_dates


MONTH_JP = ["", "1月", "2月", "3月", "4月", "5月", "6月",
            "7月", "8月", "9月", "10月", "11月", "12月"]


def days_str(days, estimated=False):
    suffix = "*" if estimated else ""
    return ", ".join(f"{d}日{suffix}" for d in days)


def render_year_table(year, by_month, is_estimated_year=False, is_current_year=False):
    lines = []
    total = sum(len(v) for v in by_month.values())
    year_label = f"{year}年（{'集計中' if is_current_year else f'{total}回'}）"
    lines.append(f"## {year_label}")
    lines.append("")
    if is_estimated_year:
        lines.append("> 3月〜7月3日はテーブル形式の記録なし。初回は3月27日、以降「毎週日曜日」と記載されていたため推定（*）。")
        lines.append("")
    lines.append("| 月 | 日程 | 回数 |")
    lines.append("|----|------|------|")
    for month in sorted(by_month):
        days = sorted(by_month[month])
        estimated = is_estimated_year and year == 2022 and month <= 7
        lines.append(f"| {MONTH_JP[month]} | {days_str(days, estimated)} | {len(days)} |")
    if not is_current_year:
        lines.append(f"| **合計** | | **{total}** |")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def generate_markdown(past_dates, today):
    by_year = defaultdict(lambda: defaultdict(list))
    for d in past_dates:
        by_year[d.year][d.month].append(d.day)

    summary_rows = []
    grand_total = 0
    for year in sorted(by_year):
        count = sum(len(v) for v in by_year[year].values())
        if year < today.year:
            grand_total += count
            note = " (うち15件は推定)" if year == 2022 else ""
            summary_rows.append(f"| {year} | {count}{note} |")
        else:
            summary_rows.append(f"| {year} | 集計中 |")

    summary = "\n".join(summary_rows)

    body_parts = []
    for year in sorted(by_year):
        is_current = (year == today.year)
        body_parts.append(render_year_table(
            year,
            by_year[year],
            is_estimated_year=(year == 2022),
            is_current_year=is_current,
        ))

    return f"""+++
title = "開催歴"
date = "2022-03-27T00:00:00+09:00"
author = "Michael Cashen"
authorTwitter = "michaelcashen"
cover = ""
description = "三浦コンピュータクラブの過去セッション一覧"
showFullContent = true
readingTime = false
+++

Generated from git history of `content/posts/home.md`.
Sessions marked with * are **estimated** (pre-table era: described as "every Sunday" in early commits, no formal schedule table yet).

---

## セッション数サマリー

| 年 | セッション数 |
|------|------|
{summary}
| **合計** | **{grand_total}+** |

---

{("".join(body_parts)).rstrip()}

---

*Source: git log of `content/posts/home.md` — all dates that appeared as 開催 in the schedule table, filtered to past dates only.*
"""


def main():
    today = date.today()
    print("Scanning git history...", file=sys.stderr)
    all_dates = get_all_session_dates()
    past_dates = sorted(d for d in all_dates if d <= today)
    print(f"Found {len(past_dates)} past sessions.", file=sys.stderr)
    md = generate_markdown(past_dates, today)
    with open(HISTORY_MD, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Updated {HISTORY_MD}", file=sys.stderr)


if __name__ == "__main__":
    main()
