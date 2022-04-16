# Тимофей спросил у Гоши,
# умеет ли тот работать с числами в двоичной системе счисления.
# Он ответил, что проходил это на одной из первых лекций по информатике.
# Тимофей предложил Гоше решить задачку.
# Два числа записаны в двоичной системе счисления.
# Нужно вывести их сумму, также в двоичной системе.
# Встроенную в язык программирования возможность
# сложения двоичных чисел применять нельзя.

# Решение должно работать за O(N),
# где N –— количество разрядов максимального числа на входе.

# Формат ввода
# Два числа в двоичной системе счисления, каждое на отдельной строке.
# Длина каждого числа не превосходит 10 000 символов.

# Формат вывода
# Одно число в двоичной системе счисления.

from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    result = ''
    remainder = False
    len_first = len(first_number)
    len_second = len(second_number)
    if len_first < len_second:
        raznica = len_second - len_first
        list_first = ['0'] * raznica
        list_first.extend(list(first_number))
        first_number = ''.join(list_first)
    elif len_first > len_second:
        raznica = len_first - len_second
        list_second = ['0'] * raznica
        list_second.extend(list(second_number))
        second_number = ''.join(list_second)

    for index, num in enumerate(first_number[::-1]):
        num_1 = int(num)
        num_2 = int(second_number[::-1][index])
        if num_1 == num_2:
            if num_1 == 1:

                if remainder:
                    result += '1'
                    if index == len(first_number) - 1:
                        result += '1'
                else:
                    result += '0'
                    remainder = True
                    if index == len(first_number) - 1:
                        result += '1'
            elif num_1 == 0:
                if remainder:
                    result += '1'
                    remainder = False
                else:
                    result += '0'
        else:
            if remainder:
                result += '0'
                if index == len(first_number) - 1:
                    result += '1'
            else:
                result += '1'
    return result[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
