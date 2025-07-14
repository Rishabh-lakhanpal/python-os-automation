#!/usr/bin/env python3

word = "Python"
filename = "sample.txt"

with open(filename, "r") as file:
    content = file.read()

count = content.lower().count(word.lower())
print(f"🔍 The word '{word}' appeared {count} times.")
