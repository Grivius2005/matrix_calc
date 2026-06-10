from matrix import Matrix
from memory import Memory


def print_matrix(m):
    for row in m.data:
        for value in row:
            print(value, end="  ")
        print("")
    print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("testy: ")
    mat1 = Matrix(rows=3, cols=3)
    mat2 = Matrix(rows=2, cols=3)
    mat3 = Matrix([[1, 2],
                   [3, 4]])
    mat4 =  Matrix([[2, 6],
                    [3, 4]])

    mat5 = Matrix([[1, 2, 1],
                   [3, 2, 1]])

    mat6 = Matrix([[1, 2, 1],
                   [3, 2, 1],
                   [2, 5, 7]])
    mat7 = Matrix([[1, 5, 2, 4],
                   [3, 1, 0, 0],
                   [2, 4, 6, 7],
                   [1, 0, 0, 0]])

    try:
        print(mat1.trace())
    except ValueError as e:
        print(e)
    try:
        print(mat2.trace())
    except ValueError as e:
        print(e)
    try:
        print(mat3.trace())
    except ValueError as e:
        print(e)
    try:
        print(mat4.trace())
    except ValueError as e:
        print(e)
    try:
        print(mat5.trace())
    except ValueError as e:
        print(e)
    try:
        print(mat6.trace())
    except ValueError as e:
        print(e)
    try:
        print(mat7.trace())
    except ValueError as e:
        print(e)