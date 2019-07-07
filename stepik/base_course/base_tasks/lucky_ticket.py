a = int(input())
sum1 = a % 10 + a % 100 // 10 + a % 1000 // 100
sum2 = a // 100000 + a // 10000 % 10 + a // 1000 % 10
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')

print(sum2, sum1)