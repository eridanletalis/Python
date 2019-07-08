a = input()
s = a.lower()

k = 0
for i in s:
    if i == 'g' or i == 'c':
        k += 1
print((k / len(a)) * 100)