def problem(a):
    if not isinstance(a, int):
        return 'Error'
    else:
        return a * 50 + 6


if __name__ == '__main__':
    print(problem(1))
