from bisect import bisect_left


def binary_search(an_iterble, target):
    index = bisect_left(an_iterble, target)
    if index <= len(an_iterble) and an_iterble[index] == target:
        return True
    return False

# def binary_search(a_list, n):
#     first = 0
#     last = len(a_list) - 1
#     while last >= first:
#         mid = (first + last) // 2
#         if a_list[mid] == n:
#             return True
#         else:
#             if n < a_list[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return False
