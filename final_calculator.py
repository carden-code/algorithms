# 68359374  
from operator import add, floordiv, mul, sub

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}


def read_input() -> list:
    return input().strip().split()


def polish_notation(subsequence: list) -> int:
    stack = []

    for s in subsequence:
        try:
            if type(int(s)) == int:
                stack.append(s)
        except ValueError:
            num_1, num_2 = int(stack.pop()), int(stack.pop())
            stack.append(OPERATORS[s](num_2, num_1))

    return stack.pop()


if __name__ == '__main__':
    string = read_input()
    print(polish_notation(string))
