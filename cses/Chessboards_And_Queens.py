reserv = []
i = 0
for inp in open('input.txt', 'r'):
    for idx, val in enumerate(inp):
        if val == '*':
            reserv.append((i, idx))
    i += 1

import numpy as np
grid = np.zeros([8,8], dtype=int)

     



