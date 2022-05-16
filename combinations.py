def read_input() -> str:
    return input()


def combo(nums, start_nums=0, string=''):
    """ Displays all possible combinations of
    letters according to the given numbers
    on the phone keypad. """
    count = len(nums)
    if start_nums == count:
        print(string, end=' ')
    else:
        chars = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        num = int(nums[start_nums])
        for char in chars[num]:
            combo(nums, start_nums + 1, string + char)


if __name__ == '__main__':
    number = read_input()
    combo(nums=number)
