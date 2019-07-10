def closest_mod_5(x):
    while True:
        if x % 5 == 0:
            return x
        else:
            x += 1


x = 31
a = closest_mod_5(x)
print(a)
