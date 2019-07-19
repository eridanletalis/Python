def binary_search(num, sorted_list):
    a, b = 0, len(sorted_list) - 1
    while a <= b:
        m = a + (b - a)//2
        if sorted_list[m] == num:
            return m
        elif sorted_list[m] > num:
            b = m - 1
        elif sorted_list[m] < num:
            a = m + 1
    return -1


def main():
    init_list = [int(x) for x in input().split()][1:]
    init_list.sort()
    nums_to_search = [int(x) for x in input().split()][1:]
    for num in nums_to_search:
        print(binary_search(num, init_list), end=" ")


if __name__ == "__main__":
    main()