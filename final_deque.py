class Deque:
    def __init__(self, max_size: int) -> None:
        self.queue: list = [None] * max_size
        self.max_n: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_overflowed(self) -> bool:
        return self.size == self.max_n

    def push_back(self, value: int) -> None:
        if self.is_overflowed():
            raise IndexError('Deque overflowing')
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_front(self, value: int) -> None:
        if self.is_overflowed():
            raise IndexError('Deque overflowing')
        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_n
        self.size += 1

    def pop_front(self) -> None:
        if self.is_empty():
            raise IndexError('Deque is empty')
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return value

    def pop_back(self) -> None:
        if self.is_empty():
            raise IndexError('Deque is empty')
        value = self.queue[self.tail - 1]
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return value


def main() -> None:
    number_commands = int(input())
    max_size = int(input())
    my_dec = Deque(max_size=max_size)

    for _ in range(number_commands):
        list_command = input().split()
        if list_command[0] == 'push_back':
            value = int(list_command[1])
            try:
                my_dec.push_back(value)
            except IndexError:
                print('error')
        elif list_command[0] == 'push_front':
            value = int(list_command[1])
            try:
                my_dec.push_front(value)
            except IndexError:
                print('error')
        elif list_command[0] == 'pop_front':
            try:
                print(my_dec.pop_front())
            except IndexError:
                print('error')
        elif list_command[0] == 'pop_back':
            try:
                print(my_dec.pop_back())
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()
