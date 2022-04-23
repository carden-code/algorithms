# Гоша и Тимофей нашли необычный тренажёр
# для скоростной печати и хотят освоить его.
# Тренажёр представляет собой поле из клавиш 4× 4,
# в котором на каждом раунде появляется конфигурация цифр и точек.
# На клавише написана либо точка, либо цифра от 1 до 9.
# В момент времени t игрок должен одновременно нажать на все клавиши,
# на которых написана цифра t. Гоша и Тимофей могут нажать в один момент
# времени на k клавиш каждый.
# Если в момент времени t были нажаты все нужные клавиши,
# то игроки получают 1 балл.

# Найдите число баллов, которое смогут заработать Гоша и Тимофей,
# если будут нажимать на клавиши вдвоём.

# Формат ввода
# В первой строке дано целое число k (1 ≤ k ≤ 5).
# В четырёх следующих строках задан вид тренажёра –—
# по 4 символа в каждой строке. Каждый символ —– либо точка,
# либо цифра от 1 до 9.
# Символы одной строки идут подряд и не разделены пробелами.

# Формат вывода
# Выведите единственное число –— максимальное количество баллов,
# которое смогут набрать Гоша и Тимофей.
# Пример 2
# Ввод:	 Вывод:
# 4           1
# 1111
# 9999
# 1111
# 9911

from typing import List, Tuple


def sleight_of_hand(character_list: List[str], number_clicks: int) -> int:
    """
    This function takes a list of characters and the number of clicks,
        in a loop counts the number of each character in the list and
        compares it with the number of clicks multiplied by 2,
        and if the number of characters is more than 1 and
        not more than the number of clicks, then 1 point is assigned.
        Returns an integer number of points.
    """
    result = 0
    for s in set(character_list):
        if s != '.' and character_list.count(s) <= number_clicks * 2:
            result += 1
    return result


def read_input() -> Tuple[List[str], int]:
    """
    This function reads data from standard input and
        returns a list of characters and a K number.
    """
    number_clicks = int(input())
    number_of_lines = 4
    result = ''
    while number_of_lines:
        result += input().strip()
        number_of_lines -= 1
    return list(result), number_clicks


char_list, clicks = read_input()

print(sleight_of_hand(character_list=char_list, number_clicks=clicks))
