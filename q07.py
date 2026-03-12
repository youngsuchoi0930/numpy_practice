import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)


# Q1. array에 5를 더한 값을 출력해보세요.
plus = array + 5
print(plus)

# Q2. array에 5를 뺀 값을 출력해보세요.
minus = array - 5
print(minus)
# Q3. array에 5를 곱한 값을 출력해보세요.
gop = array * 5
print(gop)
# Q4. array를 5로 나눈 값을 출력해보세요.
div = array / 5
print(div)
# Q5. array에 array2를 더한 값을 출력해보세요.
array2 = np.array([5, 4, 3, 2, 1])

array3 = array2 + array
print(array3)

# Q6. array에 array2를 뺀 값을 출력해보세요.

array3 = array - array2
print(array3)
