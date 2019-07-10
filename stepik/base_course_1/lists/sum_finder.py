a = input().split()
result = ''
for i in range(len(a)):
    if len(a) == 1:
        result += a[i]
    else:
        if i != len(a) - 1:
            t = int(a[i - 1]) + int(a[i + 1])
            result += str(t) + " "
        else:
            t = int(a[i - 1]) + int(a[0])
            result += str(t)
print(result)