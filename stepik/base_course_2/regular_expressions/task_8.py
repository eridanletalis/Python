# найти и поменять местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.

import sys
import re

pattern = r'\b(\w)(\w)(\w*)\b'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r'\2\1\3', line))