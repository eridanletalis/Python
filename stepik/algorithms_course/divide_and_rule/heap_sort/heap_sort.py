from heapq import heappush, heappop
from random import randint


def heap_sort(array):
    h = []
    for i in array:
        heappush(h, i)
    for i in range(len(h)):
        array[i] = heappop(h)


def main():
    a = []
    for i in range(10000000):
        s = randint(0, 10000000)
        a.append(s)
    print(a)
    heap_sort(a)
    print(a)


if __name__ == '__main__':
    main()
