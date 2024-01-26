#!/usr/bin/python3

import sys
import signal

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        print("{}: {}".format(status_code, status_codes[status_code]))

def signal_handler(signum, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Setup signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split(" ")
        if len(parts) < 2:
            continue

        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except ValueError:
            continue

        if status_code in status_codes:
            status_codes[status_code] += 1
            total_size += file_size

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)
