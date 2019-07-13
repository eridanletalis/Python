# найти и заменить в строке слово 'human' на 'computer'

import sys
import re

pattern = r'human'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'computer', line))