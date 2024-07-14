# Создаем функцию с параметрами
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        if i == 0 or i > 0:
            i += 1
        else:
            matrix.append([])
        for j in range(m):
            if j == 0:
                j += 1
            else:
                matrix.append([value] * m)
    print(matrix)
    return matrix

get_matrix(2, 2, 10)


