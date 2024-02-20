from collections import deque
import random


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

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False


a_list = LinkedList()
for i in range(0, 101):
    j = random.randint(1, 100)
    a_list.append(j)
    print(j, end=" ")
print(a_list.search(1))