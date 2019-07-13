# найти строки, где 'cat' встречается более 2 раз

import sys
import re

pattern = r"(.*cat.*){2}"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print(line)