a = [int(input())]

sum = a[0]
while sum != 0:
    a.append(int(input()))
    sum += a[-1]
sum = 0
for i in a:
    sum += i * i
print(sum)
