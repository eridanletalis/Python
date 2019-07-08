a = input()
k = 0
m = ''
result = ''

for i in range(len(a)):
    if len(a) == 1:
        result += a[i] + str(1)
    if a[i] == m:
        if i != len(a) - 1:
            k += 1
        else:
            k += 1
            result += a[i] + str(k)
    else:
        if m == '':
            m = a[i]
            k += 1
        else:
            result += m + str(k)
            m = a[i]
            k = 1
            if i == len(a) - 1:
                result += a[i] + str(1)
print(result)