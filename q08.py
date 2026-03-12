import numpy as np

"""
[[0]
 [1]
 [2]
 [3]
 [4]
 [5]] 배열 A와

 [0 1 2 3 4 5] 배열 B를 선언하고, 덧셈 연산해보세요.
"""
array_A = np.arange(0, 6).reshape(6, 1)
# print(array_A)

array_B = np.arange(0, 6).reshape(1, 6)
# print(array_B)

array_sum = np.add(array_A, array_B)
print(array_sum)
