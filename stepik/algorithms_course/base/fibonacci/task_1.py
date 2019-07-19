# Достаем n-ый элемент последовательности
class Example:
    pass


def fib(n):
    if n <= 1:
        return 1
    else:
        return round(1 / (5 ** 0.5) * (((1 + (5 ** 0.5)) / 2) ** n + ((1 - (5 ** 0.5)) / 2) ** n)) % 10


for i in range(1, 41):
    print(fib(i))
