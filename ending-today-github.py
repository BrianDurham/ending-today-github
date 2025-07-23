#!/usr/bin/env python3
"""
ending-today-github.py

Parse Estibot "ending today" CSV files and print available domains (via `tldx`) sorted by appraised value.

Author: Brian Durham
License: MIT
Website: https://briandurham.net

Need a custom domain scouting script or tool like this one? I’m available for freelance Python and automation projects.
Support my work: https://ko-fi.com/BrianDurham
"""

import csv
import sys
import subprocess

def is_available_with_tldx(domain):
    try:
        result = subprocess.run(["tldx", domain], capture_output=True, text=True)
        return "is available" in result.stdout.lower()
    except Exception as e:
        print(f"⚠️  Error checking {domain}: {e}")
        return False

def load_estibot_csv(filepath):
    with open(filepath, newline='', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                domain = row['domain'].strip().lower()
                value = int(row['appraised_value'].strip())
                yield {'domain': domain, 'value': value}
            except (KeyError, ValueError):
                continue

def main():
    if len(sys.argv) < 2:
        print("Usage: python estibot_tldx_mvp.py <file.csv>")
        sys.exit(1)

    csv_file = sys.argv[1]
    domains = list(load_estibot_csv(csv_file))
    domains.sort(key=lambda d: d['value'], reverse=True)

    for item in domains:
        domain = item['domain']
        value = item['value']
        if is_available_with_tldx(domain):
            print(f"{domain:<30} ${value}")

if __name__ == "__main__":
    main()
