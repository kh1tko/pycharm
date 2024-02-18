numbers = []

while True:
    num_input = input()

    if num_input.lower() == 'done':
        break

    try:
        num = int(num_input)
        numbers.append(num)
    except ValueError:
        print('Invalid input')

if numbers:
    print("Maximum", max(numbers))
    print("Minimum", min(numbers))





