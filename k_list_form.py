# Вася просил Аллу помочь решить задачу. На этот раз по информатике.

# Для неотрицательного целого числа X списочная форма –—
# это массив его цифр слева направо. К примеру,
# для 1231 списочная форма будет [1,2,3,1].
# На вход подается количество цифр числа Х, списочная форма
# неотрицательного числа Х и неотрицательное число K.
# Числа К и Х не превосходят 10000.

# Нужно вернуть списочную форму числа X + K.

# Формат ввода
# В первой строке — длина списочной формы числа X.
# На следующей строке —
# сама списочная форма с цифрами записанными через пробел.

# В последней строке записано число K, 0 ≤ K ≤ 10000.

# Формат вывода
# Выведите списочную форму числа X+K.

from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    # connected_numbers = int(''.join(map(str, number_list))) + int(k)
    # return list(map(int, str(connected_numbers)))
    return list(map(int, str(int(''.join(map(str, number_list))) + int(k))))


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
