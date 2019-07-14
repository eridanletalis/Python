from xml.etree import ElementTree

a = input()
tree = ElementTree.fromstringlist(a)

for i in tree:
    print(tree.attrib)
