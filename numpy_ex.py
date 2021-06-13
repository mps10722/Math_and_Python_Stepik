import numpy as np

A1 = np.array((-1, 2))
A2 = np.array((2, 3))
A3 = np.array((5, 4))

a = np.linalg.norm(A1 - A2)
b = np.linalg.norm(A1 - A3)
c = np.linalg.norm(A2 - A3)
s = (a + b + c) / 2
a = np.sqrt(s * (s - a) * (s - b) * (s - c))

print(round(a, 4))
