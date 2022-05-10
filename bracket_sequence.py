# Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
# Если вы с ней ещё не сталкивались,
# то наверняка столкнётесь –— она довольно популярная.

# Дана скобочная последовательность. Нужно определить, правильная ли она.

# Будем придерживаться такого определения:

# пустая строка —– правильная скобочная последовательность;
# правильная скобочная последовательность, взятая в скобки одного типа,
# –— правильная скобочная последовательность;
# правильная скобочная последовательность с приписанной слева или
# справа правильной скобочной последовательностью —– тоже правильная.
# На вход подаётся последовательность из скобок трёх видов: [], (), {}.
# Напишите функцию is_correct_bracket_seq, которая принимает на вход
# скобочную последовательность и возвращает True,
# если последовательность правильная, а иначе False.

# Формат ввода
# На вход подаётся одна строка, содержащая скобочную последовательность.
# Скобки записаны подряд, без пробелов.

# Формат вывода
# Выведите «True» или «False».

def read_input() -> str:
    return input().strip()


def is_correct_bracket_seq(brackets: str) -> bool:
    """The is_correct_bracket_seq function takes
        a bracket sequence as input and returns True
        if the sequence is correct, False otherwise."""
    result = []
    open_breacket = '({['
    close_breacket = ')}]'
    for s in brackets:
        if s in open_breacket:
            result.append(s)
        elif s in close_breacket and result:
            if s == close_breacket[0] and result[-1] == open_breacket[0]:
                result.pop()
            elif s == close_breacket[1] and result[-1] == open_breacket[1]:
                result.pop()
            elif s == close_breacket[2] and result[-1] == open_breacket[2]:
                result.pop()
            else:
                return False
        else:
            return False
    if result:
        return False
    return True


if __name__ == '__main__':
    bracket_seq = read_input()
    print(is_correct_bracket_seq(bracket_seq))
