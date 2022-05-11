# Любимый вариант очереди Тимофея — очередь,
# написанная с использованием связного списка. Помогите ему с реализацией.
# Очередь должна поддерживать выполнение трёх команд:

# get() — вывести элемент, находящийся в голове очереди, и удалить его.
# Если очередь пуста, то вывести «error».
# put(x) — добавить число x в очередь
# size() — вывести текущий размер очереди

# Формат ввода
# В первой строке записано количество команд n, не превосходящее 1000.
# В каждой из следующих n строк записаны команды по одной строке.

# Формат вывода
# Выведите ответ на каждый запрос по одному в строке.

class ListQueue:
    class Node:
        def __init__(self, value=None, next_item=None):
            self.value = value
            self.next_item = next_item

        def __str__(self) -> str:
            return str(self.value)

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'

        if self.size == 1:
            x = self.head
            self.head = self.Node()
            self.tail = self.Node()
            self.size -= 1
            return x

        if self.size == 2:
            x = self.head
            self.head = self.tail
            self.size -= 1
            return x

        x = self.head
        self.head = self.tail.next_item.next_item
        self.tail.next_item = self.head
        self.size -= 1
        return x

    def put(self, x):
        if self.size == 0:
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next_item = self.Node(value=x)
            self.tail.next_item.next_item = self.head
            self.tail = self.tail.next_item
        self.size += 1


if __name__ == '__main__':
    number_commands = int(input())
    my_queue = ListQueue()

    for _ in range(number_commands):
        list_command = input().split()
        if list_command[0] == 'put':
            number = int(list_command[1])
            my_queue.put(number)
        elif list_command[0] == 'get':
            print(my_queue.get())
        elif list_command[0] == 'size':
            print(my_queue.size)
