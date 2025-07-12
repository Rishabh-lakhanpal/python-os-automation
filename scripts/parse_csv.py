#!/usr/bin/env python3

import csv

with open("csv_file.txt") as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        name, phone, role = row
        print(f"Name: {name.strip()}, Phone: {phone.strip()}, Role: {role.strip()}")
