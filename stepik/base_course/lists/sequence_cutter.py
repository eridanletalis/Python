a = int(input())
k1 = 1
k2 = 0
result = ''
while True:
    for i in range(k1):
        result += str(k1) + " "
        k2 += 1
        if k2 == a:
            break
    if k2 == a:
        break
    k1 += 1
print(result)