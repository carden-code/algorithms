# Реализуйте класс StackMaxEffective,
# поддерживающий операцию определения максимума среди элементов в стеке.
#  Сложность операции должна быть O(1).
# Для пустого стека операция должна возвращать None.
# При этом push(x) и pop() также должны выполняться за константное время.

# Формат ввода
# В первой строке записано одно число n — количество команд,
# которое не превосходит 10000. В следующих n строках идут команды.
# Команды могут быть следующих видов:

# push(x) — добавить число x в стек;
# pop() — удалить число с вершины стека;
# get_max() — напечатать максимальное число в стеке;

# Если стек пуст, при вызове команды get_max()
#  нужно напечатать «None», для команды pop() — «error».

# Формат вывода
# Для каждой команды get_max() напечатайте результат её выполнения.
# Если стек пустой, для команды get_max() напечатайте «None».
# Если происходит удаление из пустого стека — напечатайте «error».

class StackMaxEffective:
    def __init__(self) -> None:
        self.items = []
        self.max_elem = None

    def push(self, item: int) -> None:
        if self.max_elem is None:
            self.max_elem = item
        elif item > self.max_elem:
            self.max_elem = item
        self.items.append(self.max_elem)

    def pop(self) -> None:
        if self.items:
            self.items.pop()
            self.max_elem = self.items[-1] if self.items else None
        else:
            print('error')

    def get_max(self) -> None:
        print(self.max_elem) if self.items else print(None)


stack = StackMaxEffective()

for _ in range(int(input())):
    list_command = input().split()
    if list_command[0] == 'push':
        stack.push(int(list_command[1]))
    elif list_command[0] == 'pop':
        stack.pop()
    elif list_command[0] == 'get_max':
        stack.get_max()
