# Метеорологическая служба вашего города
# решила исследовать погоду новым способом.
# Под температурой воздуха в конкретный день
# будем понимать максимальную температуру в этот день.

# Назовём хаотичностью погоды за n дней количество дней,
# в которые

# температура строго больше, чем в день до (если такой существует)
# и в день после текущего (если такой существует).

# Например, если за 5 дней максимальная температура воздуха
# составляла [1, 2, 5, 4, 8] градусов, то хаотичность за этот период
# равна 2: в 3-й и 5-й дни выполнялись описанные условия.
# Определите по ежедневным показаниям
# температуры хаотичность погоды за этот период.

# Заметим, что если число показаний n=1, то единственный день будет хаотичным.

# Формат ввода
# В первой строке дано число n –— длина периода измерений в днях,
# 1 ≤ n≤ 105. Во второй строке даны n целых чисел –—
# значения температуры в каждый из n дней.
# Значения температуры не превосходят 273 по модулю.

# Формат вывода
# Выведите единственное число — хаотичность за данный период.

from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    result = 0
    for index, _ in enumerate(temperatures):
        slice = temperatures[index:index + 3]
        if len(slice) == 3:
            if slice[0] < slice[1] > slice[2]:
                result += 1
        elif len(temperatures) == 1:
            result = 1
    else:
        if len(temperatures) > 1:
            if temperatures[0] > temperatures[1]:
                result += 1

            if temperatures[-1] > temperatures[-2]:
                result += 1
    return result


def read_input() -> List[int]:
    n = int(input())
    return list(map(int, input().strip().split()))


temperatures = read_input()
print(get_weather_randomness(temperatures))
