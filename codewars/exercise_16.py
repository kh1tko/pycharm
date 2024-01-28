def solution(number):
    if number < 0:
        return 0
    else:
        count = list(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
        return count


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


if __name__ == '__main__':
    # print(solution(88))
    print(count_by(2, 5))
