def square_digits(num: int):
    str_num = str(num)
    total = [int(i) ** 2 for i in str_num]
    total2 = ''.join(map(str, total))
    return int(total2)


products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())

try:
    chosen_product = products[choice_index]
    print("You have chosen:", chosen_product)
except IndexError:
    print("Invalid index")
finally:
    print("Execution completed.")

if __name__ == '__main__':
    print(square_digits(9119))
