a = [int(i) for i in input().split()]
b = int(input())
result = ''

for i in range(len(a)):
    if b == a[i]:
        result += str(i) + " "
if result != '':
    print(result)
else:
    print("Отсутствует")