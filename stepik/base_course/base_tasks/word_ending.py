a = int(input())
if (a % 10 == 1) and not(a % 100 == 11):
    print(a, 'программист')
elif (2 <= a % 10 <= 4) and not(11 <= a % 100 <= 19):
    print(a, 'программиста')
elif True:
    print(a, 'программистов')