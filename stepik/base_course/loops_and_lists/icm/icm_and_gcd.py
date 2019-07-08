x = int(input())
y = int(input())
a = x
b = y
r = 1
gcd = 1
if x == 0 and y == 0:
    print("asdasd")
elif x > y:
    while r != 0:
        gcd = r
        r = a % b
        a = b
        b = r
elif y > x:
    while r != 0:
        gcd = r
        r = b % a
        b = a
        a = r
elif x == y:
    gcd = x


icm = (x * y) // gcd
print(icm, x, y)
