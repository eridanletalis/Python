s = input()
a = input()
b = input()

max_iters = 1000
k = 0

while a in s:
    k += 1
    if k <= max_iters:
        s = s.replace(a, b)
    else:
        break
if k > max_iters:
    print('Impossible')
else:
    print(k)