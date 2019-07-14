from xml.etree import ElementTree


def ex_counter(tree, d, k=2):
    for child in tree:
        if not d.get(child.attrib['color']):
            d[child.attrib['color']] = k
            ex_counter(child, d, k=k+1)
        else:
            d[child.attrib['color']] += k
            ex_counter(child, d, k=k+1)


a = input()
d = {}
tree = ElementTree.fromstring(a)
d[tree.attrib["color"]] = 1
ex_counter(tree, d)
print(d['red'], d['green'], d['blue'])