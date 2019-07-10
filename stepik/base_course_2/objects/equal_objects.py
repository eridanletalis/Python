# считаем кол-во различных объектов в списке

objects = [1, 2, 3, 4, 1, 5, 3, 4, 5, 5, 5]
set = set()
for i in objects:
    set.add(id(i))
print(len(set))