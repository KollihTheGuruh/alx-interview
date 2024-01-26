# 0x03. Log Parsing

This project focuses on algorithm development and Python programming.

## Tasks

### 0. Log Parsing (Mandatory)

**Objective:** Write a script that reads `stdin` line by line and computes metrics.

#### Input Format

- `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- Lines not matching this format must be skipped.

#### Output

- After every 10 lines or a keyboard interruption (CTRL + C), print the following statistics from the beginning:
  - **Total file size:** `File size: <total size>` where `<total size>` is the sum of all previous `<file size>` values.
  - **Number of lines by status code:**
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
    - Print `<status code>: <number>` for each status code, in ascending order.
    - Skip printing for status codes that don't appear or are not integers.

#### Example

- Script to generate logs (`0-generator.py`):

```python
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
