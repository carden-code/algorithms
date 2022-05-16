def read_input() -> int:
    return int(input())


def gen_bracket(count, s='', left=0, right=0):
    """ The function should print all possible bracket
    sequences of the given length in alphabetical
    (lexicographical) order. """
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            gen_bracket(count, s + '(', left + 1, right)
        if right < left:
            gen_bracket(count, s + ')', left, right + 1)


if __name__ == '__main__':
    count = read_input()
    gen_bracket(count=count)
