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
print(triplet_sum([-1, 0, 1, 1, 1, 2, 2, 2, -1, -4], 0))  # [[-1, -1, 2], [-

print(triplet_sum([0, 0, 0, 0, 0], 0))  # [[-2, 1, 1]]
