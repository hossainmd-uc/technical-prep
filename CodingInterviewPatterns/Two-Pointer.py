# Triplet Sum


def triplet_sum(arr, target_sum):
    # a + b  + c = 0
    # reform to a + b = -c

    # sort the array
    arr.sort()

    triplets = []

    c_index = len(arr) - 1

    while len(arr) > 2 and c_index >= 2:
        c = arr[c_index]

        if c_index + 1 < len(arr) and arr[c_index + 1] == c:
            c_index -= 1
            continue

        target = target_sum - c

        # find a and b such that a + b = target
        left = 0
        right = c_index - 1

        while left < right:
            a = arr[left]
            b = arr[right]

            # if c == a:
            #     left += 1
            #     continue

            sum_num = a + b
            if sum_num == target:
                if left > 0 and arr[left - 1] == a:
                    left += 1
                    continue
                triplets.append((a, b, c))
                left += 1
                right -= 1
            elif sum_num < target:
                left += 1
            else:
                right -= 1

        c_index -= 1

    return triplets


# Test Cases
# print(triplet_sum([-1, 0, 1, 1, 1, 2, 2, 2, -1, -4], 0))  # [[-1, -1, 2], [-

# print(triplet_sum([0, 0, 0, 0, 0], 0))  # [[-2, 1, 1]]

# Is Palindrome Valid
# Two Pointer Approach

import re


def is_palindrome_valid(s):

    new_s = re.sub(r"[^\w]", "", s)
    # print(new_s)

    start = 0
    end = len(new_s) - 1

    while start < end:
        if new_s[start] != new_s[end]:
            return False
        start += 1
        end -= 1
    return True


test_cases = [
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", False),
    ("!, (?)", True),
    ("12.02.2021", True),
    ("21.02.2021", False),
    ("hello, world!", False),
]

# for s, expected in test_cases:
#     result = is_palindrome_valid(s)
#     print(
#         f"Input: '{s}' | Expected: {expected} | Result: {result} | {'✅ Pass' if result == expected else '❌ Fail'}"
#     )

# Complexity Analysis -> Space: O(1) Time: O(n)

# Largest container


def largest_container(h):
    start = 0
    end = len(h) - 1

    # optimize the heights while constraining the width to decreasing

    largest = float("-inf")
    while start < end:
        area = (end - start) * min(h[start], h[end])
        if area > largest:
            largest = area

        if h[start] < h[end]:
            start += 1
        elif h[start] > h[end]:
            end -= 1
        else:
            start += 1
            end -= 1

    return largest


# print(largest_container([2, 7, 8, 3, 7, 6]))
# Complexity Analysis -> Space: O(1) Time: O(n)
