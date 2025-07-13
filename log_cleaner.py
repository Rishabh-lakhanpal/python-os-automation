#!/usr/bin/env python3

import re

def clean_log_line(line):
    # Remove or replace emails
    line = re.sub(r"[\w\.-]+@[\w\.-]+", "[REDACTED]", line)

    # Extract timestamp
    timestamp = re.search(r"[A-Z][a-z]{2} \d{1,2} \d{2}:\d{2}:\d{2}", line)
    if timestamp:
        print(f"Timestamp: {timestamp.group()}")

    # Extract Process ID
    pid = re.search(r"\[(\d+)\]", line)
    if pid:
        print(f"Process ID: {pid.group(1)}")

    # Filter for errors
    if "ERROR" in line:
        print("⚠️ ERROR Line Found:")
        print(line)

    return line

# Read and process log file
with open("log.txt", "r") as file:
    for log_line in file:
        cleaned = clean_log_line(log_line)
        print("Cleaned Line:", cleaned)
        print("-" * 40)
