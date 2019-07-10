import re

a = input()
pattern = re.compile(r'[^\w+]')
s = re.sub(pattern, '', a).lower()

if s == s[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")