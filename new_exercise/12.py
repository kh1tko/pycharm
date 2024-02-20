class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


# stack = []
# print(stack)
# stack.append('Kanye West')
# print(stack)
# stack.append('Jay-Z')
# print(stack)
# stack.append('Chance the Rapper')
# print(stack)
# stack.pop()
# print(stack)


def reverse_string(a_string):
    stack = []
    string = ''
    for c in a_string:
        stack.append(c)
    for c in a_string:
        string += stack.pop()
    return string


# print(reverse_string('Artem'))
class MinStack():
    def __init__(self):
        self.main = []
        self.min = []

    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.main[-1])
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]


# min_stack = MinStack()
# min_stack.push(10)
# min_stack.push(15)
# print(min_stack.main)
# print(min_stack.min)


def check_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == '(':
            stack.append(c)
        if c == ')':
            if len(stack) == 0:
                return False
            else:
                return stack.pop()
        return len(stack) == 0


print(check_parentheses('str(1))'))  # Balanced
print(check_parentheses('(Hi!))'))  # Not balanced
