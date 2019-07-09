def f(x):
    return x


n = int(input())
d = {}

for i in range(n):
    key = int(input())
    if d.get(key) is None:
        d[key] = f(key)
    print(d[key])
