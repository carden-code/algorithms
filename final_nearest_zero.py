# Улица, на которой хочет жить Тимофей, имеет длину n,
# то есть состоит из n одинаковых идущих подряд участков.
# На каждом участке либо уже построен дом, либо участок пустой.
# Тимофей ищет место для строительства своего дома.
# Он очень общителен и не хочет жить далеко от других людей,
# живущих на этой улице.

# Чтобы оптимально выбрать место для строительства,
# Тимофей хочет для каждого участка знать расстояние
# до ближайшего пустого участка.
# (Для пустого участка эта величина будет равна нулю –—
# расстояние до самого себя).

# Ваша задача –— помочь Тимофею посчитать искомые расстояния.
# Для этого у вас есть карта улицы.
# Дома в городе Тимофея нумеровались в том порядке, в котором строились,
# поэтому их номера на карте никак не упорядочены.
# Пустые участки обозначены нулями.

# Формат ввода
# В первой строке дана длина улицы —– n (1 ≤ n ≤ 106).
# В следующей строке записаны n целых неотрицательных чисел — номера домов
# и обозначения пустых участков на карте (нули).
# Гарантируется, что в последовательности есть хотя бы один ноль.
# Номера домов (положительные числа) уникальны и не превосходят 109.

# Формат вывода
# Для каждого из участков выведите расстояние до ближайшего нуля.
# Числа выводите в одну строку, разделяя их пробелами.

from typing import List


def nearest_zero(number_list: List[int]) -> List[int]:
    """
    The function takes a list of numbers from 0 to 109,
        where each number is a segment. The number 0 means a plot
        without a house. And returns a list with the distance from
        each House to the empty lot.
    """
    number_plots = len(number_list)
    result = [0] * number_plots
    zero_indices = [i for i in range(number_plots) if number_list[i] == 0]

    for i in range(zero_indices[0], number_plots):
        if number_list[i] == 0:
            result[i] = 0
        else:
            result[i] = result[i - 1] + 1

    for i in range(zero_indices[-1], zero_indices[0], -1):
        if number_list[i] == 0:
            result[i] = 0
        else:
            result[i] = min(result[i], result[i + 1] + 1)

    for i in range(zero_indices[0] - 1, -1, -1):
        result[i] = result[i + 1] + 1
    return result


def read_input() -> List[int]:
    n = int(input())
    return list(map(int, input().strip().split()))


number_list = read_input()
print(" ".join(map(str, nearest_zero(number_list))))
