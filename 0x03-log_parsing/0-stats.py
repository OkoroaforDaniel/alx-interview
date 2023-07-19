#!/usr/bin/env python3

import sys
import datetime

# Initialize metrics variables
total_file_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            ip, _, date_str, request, status_code_str, file_size_str = line.strip().split(" ")
            date = datetime.datetime.strptime(date_str[1:], "%Y-%m-%d %H:%M:%S.%f")
            status_code = int(status_code_str)
            file_size = int(file_size_str)

            # Update total file size
            total_file_size += file_size

            # Update status codes count
            if status_code in status_codes:
                status_codes[status_code] += 1
            elif 200 <= status_code <= 500:
                status_codes[status_code] = 1

            # Print statistics every 10 lines
            if i % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_codes.keys()):
                    print(f"{code}: {status_codes[code]}")

        except (ValueError, IndexError):
            # Skip lines with incorrect format
            continue

except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print(f"\nFile size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

