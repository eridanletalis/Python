def print_max_cost(goods, w):
    goods.sort(key=lambda x: x[0]/x[1])
    cost = 0
    weight = 0
    for product in reversed(goods):
        if weight < w:
            if (w - weight) >= product[1]:
                weight += product[1]
                cost += product[0]
            else:
                weight += w - weight
                cost += product[0] / w - weight
        else:
            break
    print("%.3f" % cost)


n, w = map(int, input().split())
goods = []

for i in range(n):
    goods.append([int(i) for i in input().split()])
print_max_cost(goods, w)
