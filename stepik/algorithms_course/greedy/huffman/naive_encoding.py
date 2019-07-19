
def set_code(symbol, level, d):
    if level == 0:
        d[symbol] = '0'
    elif level < len(d.keys()) - 1:
        d[symbol] = '1' * level + '0'
    else:
        d[symbol] = '1' * level


def get_symb_codes(s):
    d = {}
    symb_count = []
    for i in s:
        if not d.get(i):
            d[i] = 1
        else:
            d[i] += 1
    for key, value in d.items():
        symb_count.append([key, value])
    symb_count.sort(key=lambda x: x[1])
    for i in range(len(symb_count)):
        set_code(symb_count[i][0], i, d)
    return d


def encode(s, d):
    res = ''
    for i in s:
        res += d[i]
    return res


s = input()
d = get_symb_codes(s)
s_encode = encode(s, d)
print(len(d), len(s_encode))
for key, value in d.items():
    print(str(key) + ": " + str(value))
print(s_encode)

