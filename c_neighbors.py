# Дана матрица.
# Нужно написать функцию, которая для элемента возвращает всех его соседей.
# Соседним считается элемент, находящийся от текущего на одну ячейку влево,
# вправо, вверх или вниз. Диагональные элементы соседними не считаются.

# Формат ввода
# В первой строке задано n — количество строк матрицы.
# Во второй — количество столбцов m. Числа m и n не превосходят 1000.
# В следующих n строках задана матрица.
# Элементы матрицы — целые числа, по модулю не превосходящие 1000.
# В последних двух строках записаны координаты элемента
# (индексация начинается с нуля), соседей которого нужно найти.

# Формат вывода
# Напечатайте нужные числа в возрастающем порядке через пробел.

from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    # Здесь реализация вашего решения
    result = []
    try:
        if col:
            result.append(matrix[row][col - 1])
    except Exception:
        pass

    try:
        result.append(matrix[row + 1][col])
    except Exception:
        pass

    try:
        if row:
            result.append(matrix[row - 1][col])
    except Exception:
        pass

    try:
        result.append(matrix[row][col + 1])
    except Exception:
        pass

    return sorted(result)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
