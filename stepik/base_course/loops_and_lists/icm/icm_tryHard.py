x = int(input())
y = int(input())
flag = True
icm = 0

while flag:
    icm += 1
    if icm % x == 0 and icm % y == 0:
        flag = False
print(icm)
