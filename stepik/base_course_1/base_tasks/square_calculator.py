name = input()
if name == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
if name == 'круг':
    r = int(input())
    pi = 3.14
    s = pi * r * r
    print(pi * r * r)
if name == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
