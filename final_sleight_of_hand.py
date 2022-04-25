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

NUMBER_OF_LINES = 4
PLAYERS = 2


def sleight_of_hand(character_list: List[str], number_clicks: int) -> int:
    """
    This function takes a list of characters and a number of clicks.
        In the loop, we go over all the elements and if the element is not
        a point and it is not in the deleted set, we add 1 to the dictionary.
        If the number of elements exceeds the number of
        clicks * on the number of players, then remove the element
        from the dictionary and add it to the deleted set.
        And return the length of the dictionary.
    """
    del_char = set()
    counnt_dict = {x: 0 for x in set(character_list) if x != '.'}
    for s in character_list:
        if s != '.' and s not in del_char:
            counnt_dict[s] += 1
            if counnt_dict[s] > number_clicks * PLAYERS:
                del_char.add(s)
                del counnt_dict[s]
    return len(counnt_dict)


def read_input() -> Tuple[List[str], int]:
    """
    This function reads data from standard input and
        returns a list of characters and a K number.
    """
    number_clicks = int(input())
    char_list = ''.join((input().strip() for _ in range(NUMBER_OF_LINES)))
    return list(char_list), number_clicks


if __name__ == '__main__':
    char_list, clicks = read_input()
    print(sleight_of_hand(character_list=char_list, number_clicks=clicks))
