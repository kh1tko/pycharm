"""
Jack really likes his number five:
the trick here is that you have to multiply
each number by 5 raised to the number of digits of each numbers,
 so, for example:

multiply(3)==15 # 3 * 5¹
multiply(10)==250 # 10 * 5²
multiply(200)==25000 # 200 * 5³
multiply(0)==0 # 0 * 5¹
multiply(-3)==-15 # -3 * 5¹
"""


def multiply(n):
    if n < 0:
        numstr1 = str(n)
        num_num2 = len(numstr1)
        result1 = n * pow(5, int(num_num2 - 1))
        return result1

    num_str = str(n)
    num_num = len(num_str)
    result = n * pow(5, int(num_num))
    return result


def multiply2(n):
    num_str = str(abs(n))
    num_len = len(num_str)

    result = n * 5 ** num_len

    return result


if __name__ == '__main__':
    print(multiply(-3))
    print(multiply2(-3))
