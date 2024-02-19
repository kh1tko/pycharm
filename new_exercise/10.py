from collections import deque


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ''
        node = self.head
        while node is not None:
            result += str(node.data) + '\n'
            node = node.next
        return result

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)


a_list = LinkedList()
a_list.append('Monday')
a_list.append('Wednesday')
print(a_list)
d = deque()
d.append('Harry')
d.append('Potter')
for item in d:
    print(item)
