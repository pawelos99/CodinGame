import numpy as np

# get all inputs
w, h = [int(i) for i in input().split()]
table = [[int(x) for x in input().split()] for _ in range(h)]
table = np.array(table)
result = np.zeros_like(table)

# loop over the table and calculate maximum possible value
# for whole table
for r, row in enumerate(table):
    for c, val in enumerate(row):
        if r == 0:
            up = 0
        else:
            up = result[r - 1, c]
        if c == 0:
            left = 0
        else:
            left = result[r, c - 1]
        result[r, c] = val + max(up, left)

print(result[-1, -1])
