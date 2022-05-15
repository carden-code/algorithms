from typing import Tuple


def read_input() -> Tuple[int, list, int]:
    days = int(input())
    money_day = list(map(int, input().strip().split()))
    price = int(input())
    return days, money_day, price


def two_bikes(arr: list, x: int, left: int, right: int):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x and (arr[mid - 1] < x or mid == 0):
        return mid + 1
    elif x <= arr[mid]:
        return two_bikes(arr, x, left, mid)
    else:
        return two_bikes(arr, x, mid + 1, right)


if __name__ == '__main__':
    n, arr, s = read_input()
    print(two_bikes(arr, s, left=0, right=n), end=' ')
    print(two_bikes(arr, s * 2, left=0, right=n))
