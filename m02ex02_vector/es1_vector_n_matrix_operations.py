import numpy as np

#ES1.1 - Length of a vector 
def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector**2))
    return len_of_vector

#ES1.2 - Dot Product
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result

#ES1.3 - Multiplying a Vector by a Matrix
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

#ES1.4 - Multiplying a Matrix by a Matrix
def matrix_multi_matrix(matrix1, matrix2):
    result = matrix1@matrix2
    return result

#ES1.5 - Matrix Inverse
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result

#MC01
vector = np.array([-2, 4, 9, 21])
result1 = compute_vector_length(vector)
print(f'1d) {result1}')

#MC02
v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result2 = compute_dot_product(v1, v2)
print(f'2b) {result2}')

#MC03
x1 = np.array([[1, 2], [3, 4]])
k1 = np.array([1, 2])
result3 = x1.dot(k1)
print(f'3a) {result3}')

#MC04
x2 = np.array([[-1, 2], [3, -4]])
k2 = np.array([1, 2])
result4 = x2@k2
print(f'4b) {result4}')

#MC05
m1 = np.array([[-1, 1, 1], [0, -4, 9]])
v1 = np.array([0, 2, 1])
result5 = matrix_multi_vector(m1, v1)
print(f'5a) {result5}')

#MC06
m2 = np.array([[0, 1, 2], [2, -3, 1]])
m3 = np.array([[1, -3], [6, 1], [0, -1]])
result6 = matrix_multi_matrix(m2, m3)
print(f'6c) {result6}')

#MC07
m4 = np.eye(3)
m5 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result7 = m4@m5
print(f'7a) {result7}')

#MC08
m6 = np.eye(2)
m6 = np.reshape(m6, (-1, 4))[0]
m7 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result8 = m6@m7
print(f'8d) {result8}')

#MC09
m8 = np.array([[1, 2], [3, 4]])
m8 = np.reshape(m8, (-1, 4), "F")[0]
m9 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result9 = m8@m9
print(f'9b) {result9}')

#MC10
m10 = np.array([[-2, 6], [8, -4]])
result10 = inverse_matrix(m10)
print(f'10a) {result10}')
