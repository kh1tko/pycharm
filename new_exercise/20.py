class Stack(list):
    def push(self, item):
        self.append(item)


# Пример
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()  # -> 3
s.pop()  # -> 2


class Stack:
    def __init__(self):
        self._items = list()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)


# Пример использования
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()  # -> 3
s.pop()  # -> 2
