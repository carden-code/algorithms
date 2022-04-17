# Васе очень нравятся задачи про строки, поэтому он придумал свою.
# Есть 2 строки s и t, состоящие только из строчных букв.
# Строка t получена перемешиванием букв строки s и
# добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

# Формат ввода
# На вход подаются строки s и t, разделённые переносом строки.
# Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

# Формат вывода
# Выведите лишнюю букву.

from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    sort_longer = sorted(longer)
    sort_shorter = sorted(shorter)
    dict_str_long = {}
    dict_str_short = {}

    for s in sort_longer:
        dict_str_long[s] = sort_longer.count(s)
        dict_str_short[s] = sort_shorter.count(s)

    for key in dict_str_long:
        if dict_str_long[key] != dict_str_short[key]:
            result = key

    return result


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
