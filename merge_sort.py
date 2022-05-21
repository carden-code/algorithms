def merge(array: list, left_index: int, middle: int, right_index: int) -> list:
    """ Sorts 2 parts of an array. """
    left_copy = array[left_index:middle]
    right_copy = array[middle:right_index]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while (left_index + left_copy_index < middle and
            middle + right_copy_index < right_index):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    if left_index + left_copy_index < middle:
        while sorted_index < right_index:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            sorted_index = sorted_index + 1
    else:
        while sorted_index < right_index:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
            sorted_index = sorted_index + 1
    return array


def merge_sort(array: list, left_index: int, right_index: int) -> None:
    """ Main. """
    if right_index - left_index > 1:
        middle = (left_index + right_index) // 2
        merge_sort(array, left_index, middle)
        merge_sort(array, middle, right_index)

        merge(array, left_index, middle, right_index)
