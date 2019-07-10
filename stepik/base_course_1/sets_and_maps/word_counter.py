a = input().lower().split()
d = dict()

for key in a:
    if d.get(key) is None:
        d[key] = 1
    else:
        d[key] += 1
for key, value in d.items():
    print(key, value)