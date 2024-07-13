def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        amg = []
        matrix.append(amg)
        for j in range(m):
            amg.append(value)
    return matrix
result1 = get_matrix(15, 3, 6)
result2 = get_matrix(100, 5, 42)
result3 = get_matrix(500, 2, 13)
print(result1)
print(result2)
print(result3)