from random import randint
from stepik.algorithms_course.testing.speed_tester import compare
from stepik.algorithms_course.divide_and_rule.quick_sort.quick_sort import quick_sort
from stepik.algorithms_course.divide_and_rule.heap_sort.heap_sort import heap_sort


def run_heap(n):
    a = []
    for i in range(1000):
        s = randint(0, 1000)
        a.append(s)
    for i in range(n):
        heap_sort(a)


def run_quick2(n):
    b = []
    for i in range(1000):
        q = randint(0, 1000)
        b.append(q)
    for i in range(n):
        quick_sort(b)


compare([run_quick2, run_heap], list(range(10)))