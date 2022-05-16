from typing import Tuple


def read_input() -> Tuple[int, list]:
    number = int(input())
    list_nubers = list(map(int, input().strip().split()))
    return number, list_nubers


def bubble(n: int, array: list) -> None:
    count = 0
    count_2 = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                count += 1
        if count:
            print(*array)
            count = 0
            count_2 += 1
    if not count_2:
        print(*array)


if __name__ == '__main__':
    n, list_num = read_input()
    bubble(n=n, array=list_num)
