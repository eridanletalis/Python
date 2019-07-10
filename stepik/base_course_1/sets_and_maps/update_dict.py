def update_dictionary(d, key, value):
    if d.get(key) is None:
        if d.get(2 * key) is None:
            d[2 * key] = [value]
        else:
            d[2 * key].append(value)
    else:
        d.get(key).append(value)


d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)
