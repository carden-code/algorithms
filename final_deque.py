# 68335413
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

    def pop_front(self) -> int:
        if self.is_empty():
            raise IndexError('Deque is empty')
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return value

    def pop_back(self) -> int:
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

    commands = {
        'push_back': my_dec.push_back,
        'push_front': my_dec.push_front,
        'pop_front': my_dec.pop_front,
        'pop_back': my_dec.pop_back
    }

    for _ in range(number_commands):
        list_command = input().split()
        if len(list_command) > 1:
            try:
                commands[list_command[0]](value=list_command[1])
            except IndexError:
                print('error')
        else:
            try:
                print(commands[list_command[0]]())
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()
