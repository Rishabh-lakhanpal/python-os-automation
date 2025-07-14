#!/usr/bin/env python3
import re

def extract_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        # Simple regex for emails
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
        return emails

emails = extract_emails_from_file("sample.txt")

print("✅ Emails Found:")
for email in emails:
    print("-", email)
