from collections import Counter, namedtuple
from heapq import heapify, heappush, heappop


class Node(namedtuple("Node", ['left', 'rigth'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.rigth.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["name"])):
    def walk(self, code, acc):
        code[self.name] = acc


def huffman_encode(s):
    # h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heappop(h)
        freq2, _count2, right = heappop(h)
        heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    [(_freq, _count, root)] = h
    code = {}
    root.walk(code, "")
    return code


def decode(s_encoded, code):
    res = ''
    enc_symb = ''
    for symb in s_encoded:
        enc_symb += symb
        for dec_symb in code:
            if code.get(dec_symb) == enc_symb:
                res += dec_symb
                enc_symb = ''
                break
    return res


def main():
    s = input()
    code = huffman_encode(s)
    s_encoded = "".join(code[ch] for ch in s)
    print(len(code), len(s_encoded))
    for ch in code:
        print("{}: {}".format(ch, code[ch]))
    print(s_encoded)


if __name__ == "__main__":
    main()
