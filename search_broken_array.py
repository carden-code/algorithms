# 68547154
from typing import Tuple


def read_input() -> Tuple[int, int, list]:
    """Read input."""
    len_array = int(input())
    element = int(input())
    list_nubers = list(map(int, input().strip().split()))
    return len_array, element, list_nubers


def broken_search(array: list, search_element: int) -> int:
    """The function returns the index of the desired element,
    if there is one in the array (numbering from zero).
    If the element is not found, the function should return -1.
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == search_element:
            return middle
        if array[start] <= array[middle]:
            if array[start] <= search_element < array[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if array[middle] < search_element <= array[end]:
                start = middle + 1
            else:
                end = middle - 1
    return -1


if __name__ == '__main__':
    length_array, search_value, array = read_input()
    print(broken_search(array, search_value))
