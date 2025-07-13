#!/bin/env/python3

import sys
import re 
logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
	if "CRON" not in line:
		continueimport re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((.+)\)$"
    result = re.search(pattern, line)
    print(result[1])
    print(line.strip())
