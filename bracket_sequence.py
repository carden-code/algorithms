def is_correct_bracket_seq(brackets: str) -> bool:
    """pass"""
    if len(brackets) % 2 != 0:
        return False
    flag = True
    for i in range(len(brackets)):
        for j in range(len(brackets)):
            if brackets[i] == '(':
                


x = '{[([])]}[]{}()'

print(is_correct_bracket_seq(x))