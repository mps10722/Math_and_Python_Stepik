import numpy as np

i = 5
Z = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])

print(np.unravel_index(i, Z.shape))
