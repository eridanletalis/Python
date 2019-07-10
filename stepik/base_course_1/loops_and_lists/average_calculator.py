a = int(input())
b = int(input())

k = 0
sum = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        k += 1
print(sum / k)