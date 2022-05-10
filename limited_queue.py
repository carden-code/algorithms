# Астрологи объявили день очередей ограниченного размера.
# Тимофею нужно написать класс MyQueueSized,
# который принимает параметр max_size,
# означающий максимально допустимое количество элементов в очереди.

# Помогите ему —– реализуйте программу, которая будет эмулировать работу
# такой очереди. Функции, которые надо поддержать, описаны в формате ввода.

# Формат ввода
# В первой строке записано одно число — количество команд.
# Во второй строке задан максимально допустимый размер очереди.
# Далее идут команды по одной на строке. Команды могут быть следующих видов:

# push(x) — добавить число x в очередь;
# pop() — удалить число из очереди и вывести на печать;
# peek() — напечатать первое число в очереди;
# size() — вернуть размер очереди;
# При превышении допустимого размера очереди нужно вывести «error».
# При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
# Формат вывода
# Напечатайте результаты выполнения нужных команд, по одному на строке.

class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        return self.queue[self.head] if self.size else None


if __name__ == '__main__':
    number_commands = int(input())
    max_size = int(input())
    my_queue = MyQueueSized(max_size=max_size)

    for _ in range(number_commands):
        list_command = input().split()
        if list_command[0] == 'push':
            number = int(list_command[1])
            my_queue.push(number)
        elif list_command[0] == 'pop':
            print(my_queue.pop())
        elif list_command[0] == 'peek':
            print(my_queue.peek())
        elif list_command[0] == 'size':
            print(my_queue.size)
