from typing import Callable, List, Tuple


def read_input() -> Tuple[int, str]:
    number = int(input())
    list_nubers = input().strip().split()
    return number, list_nubers


def comparator(string_1: str, string_2: str) -> bool:
    """ pass """
    return string_1 + string_2 < string_2 + string_1


def big_number(array: List[str], func: Callable) -> str:
    """ pass """
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and func(array[j - 1], item_to_insert):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return ''.join(array)


if __name__ == '__main__':
    n, arr = read_input()
    print(big_number(arr, comparator))
