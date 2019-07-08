a = input().split()
a.sort()
m = ''
equals = False
result = ''

for i in range(len(a)):
    if i == 0:
        m = a[i]
    elif a[i] == m:
        if i != len(a) - 1:
            equals = True
        else:
            result += a[i]
    else:
        if equals:
            result += m + " "
        m = a[i]
        equals = False

print(result)