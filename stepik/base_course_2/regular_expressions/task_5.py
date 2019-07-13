# найти строки, где есть слова,состоящие из 2-ух одинаковых частей

import sys
import re

pattern = r'\b(.+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)