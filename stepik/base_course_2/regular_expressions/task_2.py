# найти строки, где 'cat' встречается в качестве отдельного слова

import sys
import re

pattern = r'(.*\bcat\b.*)'
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line):
        print(line)