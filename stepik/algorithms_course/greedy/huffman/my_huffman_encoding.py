from heapq import heapify, heappush, heappop
from collections import Counter


# создаем список листов
def get_leafs(s):
    symb_count = [(freq, ch) for ch, freq in Counter(s).items()]
    symb_count.sort(key=lambda x: (x[0], x[1]))
    return symb_count


# создаем бинарное дерево
def get_symb_tree(s):
    tree = []
    leafs = get_leafs(s)
    heapify(leafs)
    i = 0
    while leafs:
        a = heappop(leafs)
        heappush(tree, a)
        a_id = i
        i += 1
        if not leafs:
            break
        b = heappop(leafs)
        b_id = i
        i += 1
        heappush(tree, b)
        c = (a[0] + b[0], 'Node', (a_id, b_id))
        heappush(leafs, c)
    tree.sort(reverse=True)
    return tree


# задаем коды всем символам и добавляем в словарь
def set_symb_codes(tree, d, id=0, code=""):
    node = tree[id]
    if len(tree) <= 1:
        d[node[1]] = '0'
    elif node[1] == 'Node':
        set_symb_codes(tree, d, len(tree) - node[2][1] - 1, code + '0')
        set_symb_codes(tree, d, len(tree) - node[2][0] - 1, code + '1')
    else:
        d[node[1]] = code


# кодируем исходную строку
def encode(s, d):
    res = ''
    for i in s:
        res += d[i]
    return res


# декодируем исходную строку
def decode(s, d):
    res = ''
    enc_symb = ''
    for symb in s:
        enc_symb += symb
        for dec_symb in d:
            if d.get(dec_symb) == enc_symb:
                res += dec_symb
                enc_symb = ''
                break
    return res


s = input()
d = {}
tree = get_symb_tree(s)
set_symb_codes(tree, d)

s_encode = encode(s, d)
res_list = [[key, value] for key, value in d.items()]
res_list.sort(key=lambda x: x[1])
print(len(d), len(s_encode))
for i in res_list:
    print("{}: {}".format(i[0], i[1]))
print(s_encode)
print(decode(s_encode, d))

