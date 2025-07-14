#!/usr/bin/env python3

input_file = "sample.txt"
output_file = "upper_sample.txt"

with open(input_file, "r") as infile:
    content = infile.read()

with open(output_file, "w") as outfile:
    outfile.write(content.upper())

print(f"✅ Converted '{input_file}' to uppercase in '{output_file}'")

