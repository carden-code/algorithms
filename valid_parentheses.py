def is_valid(s: str) -> bool:
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        

        Example 1:

        Input: s = "()"
        Output: true
        Example 2:

        Input: s = "()[]{}"
        Output: true
        Example 3:

        Input: s = "(]"
        Output: false
        
        Runtime: 58 ms, faster than 26.96% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 13.9 MB, less than 71.96% of Python3 online submissions for Valid Parentheses.
    """
    open_breacket = '({['
    close_breacket = ')}]'
    stack = []
    for symbol in s:
        if symbol in open_breacket:
            stack.append(symbol)
        elif symbol in close_breacket and stack:
            if symbol == close_breacket[0] and stack[-1] == open_breacket[0]:
                stack.pop()
            elif symbol == close_breacket[1] and stack[-1] == open_breacket[1]:
                stack.pop()
            elif symbol == close_breacket[2] and stack[-1] == open_breacket[2]:
                stack.pop()
            else:
                return False
        else:
            return False
    if stack:
        return False
    return True

print(is_valid('{[]}'))