from typing import Tuple


def read_input() -> Tuple[int, list]:
    """ Read input. """
    number = int(input())
    list_nubers = list(map(int, input().strip().split()))
    return number, list_nubers


def sort_wardrobe(array: list) -> None:
    """ Sort (O)n """
    less = []
    equal = []
    greater = []
    for x in array:
        if x == 0:
            less.append(x)
        elif x == 1:
            equal.append(x)
        else:
            greater.append(x)
    print(*(less + equal + greater))


if __name__ == '__main__':
    n, arr = read_input()
    sort_wardrobe(arr)
