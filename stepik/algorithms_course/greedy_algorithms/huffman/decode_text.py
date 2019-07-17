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


k, l = map(int, input().split())
d = {}
for i in range(k):
    n = input().split(": ")
    d[n[0]] = n[1]
s = input()
print(decode(s, d))
