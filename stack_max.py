# Нужно реализовать класс StackMax,
# который поддерживает операцию определения максимума
#  среди всех элементов в стеке.
# Класс должен поддерживать операции push(x),
# где x – целое число, pop() и get_max().

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

class StackMax:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else print('error')

    def get_max(self):
        print(max(self.items, default=None))


stack = StackMax()

for _ in range(int(input())):
    list_command = input().split()
    if list_command[0] == 'push':
        stack.push(int(list_command[1]))
    elif list_command[0] == 'pop':
        stack.pop()
    elif list_command[0] == 'get_max':
        stack.get_max()
