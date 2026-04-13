# Pair Sum Unsorted
def pair_sum_unsorted(l, target):

    # Naive: You check each possible pair with 2 loops
    # Optimized: For any given number, you only need to check if the complement that
    # could possibly add to the target is present

    items = {}

    for i in range(len(l)):
        complement = target - l[i]
        if complement in items:
            return [i, items[complement]]
        if l[i] not in items:
            items[l[i]] = i
    return []

    # Now only need to see if complement is in the list


print(pair_sum_unsorted([-1, 3, 4, 2], 3))


def verify_soduku(b):

    # Naive: Go through every row and column for

    # Optimized: create 2 different dictionaries--one for row one for col

    # For each element you need to check if they are unique in the row and col dicts
    # Also, you need to check the 3x3 by interating over the subgrid

    rows = [set() for r in range(9)]
    cols = [set() for c in range(9)]
    # Minimally need to iterate through the items once
    sub_grid = [[set() for _ in range(3)] for _ in range(3)]

    for row in range(len(b)):
        for col in range(len(b[0])):
            item = b[row][col]
            if item in rows[row] or item in cols[col]:
                return False
            if item in sub_grid[row // 3][col // 3]:
                return False

            sub_grid[row // 3][col // 3].add(item)
            rows[row].add(item)
            cols[col].add(item)
    
    return True

            # Need to check sub grid too!
            # Given r,c, you need to find which sub grid it falls under
            # Integer divide both r,c to get top left of subgrid
