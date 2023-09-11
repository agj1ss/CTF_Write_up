#!/usr/bin/env python
import re

# Define a regular expression pattern for NANP numbering format
nanp_pattern = re.compile(r'\(\d{3}\) [2-9][0-9]{2}-[0-9]{4}')

# Open the file for reading
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
    # Iterate through each line and its line number
    for line_number, line in enumerate(file, start=1):
        # Search for the pattern in the line
        match = nanp_pattern.search(line)
        if match:
            # If a match is found, print the line and its line number
            print(f"Line {line_number}: {line.strip()}")

