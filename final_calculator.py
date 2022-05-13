# 68359374
# from operator import add, floordiv, mul, sub

# OPERATORS = {
#     '+': add,
#     '-': sub,
#     '*': mul,
#     '/': floordiv
# }
OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}


def read_input() -> list:
    """ Read input. """
    return input().strip().split()


def polish_notation(subsequence: list) -> int:
    """ The function accepts a list of characters written
    in reverse Polish notation. Numbers and arithmetic operations
    are written with a space.
    Operations can be given as input: +, -, *, / and numbers.

    Input example: 1 2 + 2 +
    Conclusion: 5.
    """
    stack = []

    for s in subsequence:
        try:
            if isinstance(int(s), int):
                stack.append(s)
        except ValueError:
            num_1, num_2 = int(stack.pop()), int(stack.pop())
            stack.append(OPERATORS[s](num_2, num_1))

    return stack.pop()


if __name__ == '__main__':
    string = read_input()
    print(polish_notation(string))
