from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple

# OrderedDict нужен для действий со словарем, где необходим порядок элементов
# Занимает память!!!

# ChainMap нужен для логического объединения словарей

# Counter нужен для подсчета элементов работает только с hashable

# defaultdict нужен для создания словаря со значением по умолчанию

# deque потокобезопасна, быстро оперирует с обеими сторонами

# namedtuple нужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом
# не изменяемый, позволяет обращаться по имени атрибута, позволяет использовать индексы

first = {1: 1, 2: 2, 3: 3}
second = {1: 1, 2: 2}
third = {4: 4, 5: 5, 6: 6}

# order1 = OrderedDict(first)
# order2 = OrderedDict(second)
# print(order1 == order2)
# order1.move_to_end(3, last=False)
# print(order1)

# chain = ChainMap(first, third)
# print(chain)
# print(5 in chain)

# counter = Counter('В лингвистике "Zero Condition" или "Zero Conditional" относится к типу условных предложений, '
#                   'которые выражают общие истины, факты или события, которые всегда происходят при определенных '
#                   'условиях. В этом типе конструкции используются Present Simple в обоих частях предложения')
# print(counter)
# print(counter.most_common(5))

# a_dict = defaultdict(list)
# for char in 'Artem':
#     a_dict[char].append(char)
# print(a_dict)

# with open('test1.txt') as file:
#     a_deque = deque(file, maxlen=2)
#     for line in a_deque:
#         print(line.rstrip())

# tom = ('Tom', 4, 'black')

Cat = namedtuple('Cat', 'name age color')
tom = Cat('Murzik', 1, 'black')
print(tom)
print(tom.age)
