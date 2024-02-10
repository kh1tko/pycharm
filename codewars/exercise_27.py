def min_sum(arr: list):
    arr.sort()
    min_sum = 0
    left, right = 0, len(arr) - 1
    while left < right:
        min_sum += arr[left] * arr[right]
        left += 1
        right -= 1
    return min_sum


if __name__ == '__main__':
    print(min_sum([5, 2, 3, 4]))
