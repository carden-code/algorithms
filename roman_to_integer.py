# Например, 2 записывается как II римскими цифрами, просто две сложенные вместе. 
# 12 записывается как XII, то есть просто X + II. 
# Число 27 записывается как XXVII, то есть XX + V + II.

# Римские цифры обычно пишутся слева направо от большего к меньшему. 
# Однако цифра четыре не IIII. Вместо этого цифра четыре пишется как IV. 
# Так как единица предшествует пятерке, мы вычитаем ее и получаем четыре. 
# Тот же принцип применим к числу девять, которое пишется как IX. 
# Есть шесть случаев, когда используется вычитание:

# I можно поставить перед V (5) и X (10), чтобы получились 4 и 9.
# X можно поставить перед L (50) и C (100), чтобы получилось 40 и 90.
# C можно поставить перед D (500) и M (1000), чтобы получились 400 и 900.
# Дана римская цифра, преобразовать ее в целое число.


def roman_to_int(num: str) -> int:
    """Input: s = "MCMXCIV"
       Output: 1994
    """
    NUMS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


    result = []
    pred_num = 0
    if len(num) == 1:
        return NUMS[num]

    for s in num:
        if pred_num and pred_num < NUMS[s]:
            if pred_num == 1 and s in ('V', 'X'):
                result.append(NUMS[s] - result.pop())
            elif pred_num == 10 and s in ('L', 'C'):
                result.append(NUMS[s] - result.pop())
            elif pred_num == 100 and s in ('D', 'M'):
                result.append(NUMS[s] - result.pop())
        else:
            result.append(NUMS[s])
        pred_num = NUMS[s]

    return sum(result)

print(roman_to_int('MCMXCIV'))
 