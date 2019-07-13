# найти и поменять местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.

import sys
import re

pattern = r"(\w)(\1)+"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r'\1', line))