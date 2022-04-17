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
    # получить бинарное число в виде массива чисел (бит)
    num1 = [*map(int, first_number)]
    num2 = [*map(int, second_number)]

    # перевернуть числа для удобства выполнения операций
    num1 = num1[::-1]
    num2 = num2[::-1]

    # дополнить числа нулями
    size = max(len(num1), len(num2))

    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))

    # сложить 2 числа
    overflow = 0
    res = []
    for obj in zip(num1, num2):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        res.append(value % 2)

    # если флаг переполнения установлен - добавить бит в начало нового числа
    if overflow == 1:
        res.append(1)

    # перевернуть число назад
    res = res[::-1]

    return ''.join(map(str, res))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
