import sys
import re

pattern = r'(cat)'
for line in sys.stdin:
    line = line.rstrip()
    print(re.findall(pattern, line))