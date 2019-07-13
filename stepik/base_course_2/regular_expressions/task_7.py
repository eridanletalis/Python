# найти и заменить первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

import sys
import re

pattern = r'\ba+\b'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'argh', line, count=1, flags=re.IGNORECASE))