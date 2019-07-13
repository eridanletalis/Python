# найти строки, где ('z' 3 буквы 'z')

import sys
import re

pattern = r'z.{3}z'
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)