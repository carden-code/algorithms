from typing import List


def read_input() -> list:
    """ Read input. """
    gardeners = int(input())
    arr = []
    for _ in range(gardeners):
        arr.append(list(map(int, input().split())))
    return arr


def clumb_creator(arr: List[list]) -> None:
    """ Print clumb. """
    begin, end = arr[0]
    for clumb in arr[1:]:
        if clumb[0] > end:
            print(begin, end)
            begin, end = clumb
        else:
            end = max(end, clumb[1])
    print(begin, end)


if __name__ == '__main__':
    sorted_arr = sorted(read_input())
    clumb_creator(sorted_arr)
