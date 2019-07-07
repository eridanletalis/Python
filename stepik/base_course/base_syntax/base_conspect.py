# Арифметические операции
# -----------------------
print(2 + 2)
print(2 * 2)
print(2 - 2)
print(2 // 2)  # - int без округления
print(2 / 2)   # - double
print(2 % 2)   # - mod
print(2 ** 5)  # - возведение в степень
# так же есть += -= *= и т.п


# Логические операции и операции сравнения
# -------------------
x = True
y = False
# (x or y), (x and y), (not x)   Приоритеты: not - 1, and - 2, or - 3
# >, <, ==, !=, <=, >=


# Типы данных
# -----------
# int, float, bool, str
# все эти типы являются неизменяемыми ???


# Преобразование типов (не изменяют аргумент)
# ------------------------------------------
x = 5
y = int(x)
z = float(x)

type(x)  #передает тип объекта


# Динамическая типизация (одна переменная может принимать значения разных типов)
# -----------------------------------------------------------------------------
a = 5
a = 'asd'
a = 5.0

q, w, e, r = True, False, True, False  #!!!!
print(not q and w or e > r)


# Ввод и вывод данных с консоли
# -----------------------------
input('write me')
s = input()
print("Your message is ", s)


# Условные операторы
# ------------------
if x % 2 == 0:
    print('четное')
elif x % 2 != 0:
    print('нечетное')
else:
    print('нечетное')


# Строки
# ------
s = 'asd'
s = "asd"
s = '''asdasd
    asdasdsad'''
s = """asdasdasd
    asdasdasd"""


# Операции со строками
# --------------------
s = "asd" + 'qw'
s = "asd" * 3
length = len(s)
# "asd" == 'asd'
# 'abc' > 'ac' - ВАЖНО! сравнение идет по первым и след. символам, где цифра < буква < БУКВА (так же по алфавиту сравнение)


# Циклы
# -----
while x > 5:
    print(x)
    x += 1