portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'MSFT', 'shares': 50, 'price': 45.67},
    {'name': 'HPE', 'shares': 75, 'price': 34.51},
    {'name': 'CAT', 'shares': 60, 'price': 67.89},
    {'name': 'IBM', 'shares': 200, 'price': 95.25}
]

print({s['name']: s['shares'] for s in portfolio})

a = 34  # Создать целое число
n = a.numerator  # Получить numerator (атрибут)
print(n)
