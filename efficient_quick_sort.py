# 68547597
def partition(persons: list, left: int, right: int) -> int:
    """Partition."""
    pivot = persons[left]
    i = left + 1
    j = right - 1
    while True:
        if i <= j and persons[j] > pivot:
            j -= 1
        elif i <= j and persons[i] < pivot:
            i += 1
        elif (persons[j] > pivot) or (persons[i] < pivot):
            continue

        if i <= j:
            persons[i], persons[j] = persons[j], persons[i]
        else:
            persons[left], persons[j] = persons[j], persons[left]
            return j


def quick_sort(persons: list, left: int, right: int) -> None:
    """Quick sort."""
    if (right - left) > 1:
        p = partition(persons, left, right)
        quick_sort(persons, left, p)
        quick_sort(persons, p + 1, right)


def transformation(persons: list) -> list:
    """Transformation."""
    persons[1] = -int(persons[1])
    persons[2] = int(persons[2])
    return [persons[1], persons[2], persons[0]]


if __name__ == '__main__':
    number = int(input())
    persons = [transformation(input().split()) for _ in range(number)]
    left = 0
    quick_sort(persons, left, len(persons))
    print(*(list(zip(*persons))[2]), sep="\n")


# from dataclasses import dataclass
#
#
# @dataclass
# class Person():
#     __slots__ = ('name', 'tasks_solved', 'fine')

#     name: str
#     tasks_solved: int
#     fine: int

#     def __post_init__(self):
#         self.tasks_solved = -int(self.tasks_solved)

#     def __lt__(self, other) -> bool:
#         return ((self.tasks_solved, self.fine, self.name) <
#                 (other.tasks_solved, other.fine, other.name))

#     def __repr__(self) -> str:
#         return self.name


# def partition(persons: list, left: int, right: int) -> int:
#     """Partition."""
#     pivot = persons[left]
#     i = left + 1
#     j = right - 1
#     while True:
#         if i <= j and persons[j] > pivot:
#             j -= 1
#         elif i <= j and persons[i] < pivot:
#             i += 1
#         elif (persons[j] > pivot) or (persons[i] < pivot):
#             continue
#         if i <= j:
#             persons[i], persons[j] = persons[j], persons[i]
#         else:
#             persons[left], persons[j] = persons[j], persons[left]
#             return j


# def quick_sort(persons: list, left: int, right: int) -> None:
#     """Quick sort."""
#     if (right - left) > 1:
#         p = partition(persons, left, right)
#         quick_sort(persons, left, p)
#         quick_sort(persons, p + 1, right)


# if __name__ == '__main__':
#     number = int(input())
#     persons = [Person(*input().split()) for _ in range(number)]
#     left = 0
#     quick_sort(persons, left, len(persons))
#     print(*persons, sep="\n")
