# module_2_5.ru

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_1 = []
        matrix.append(matrix_1)
        #print(matrix)
        for j in range(m):
            matrix_1.append(value)
        #print(matrix_1)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)


