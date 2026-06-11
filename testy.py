from matrix import Matrix
from memory import Memory


def print_matrix(m):
    for row in m.data:
        for value in row:
            print(f'{value:.1f}', end="  ")
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

    print("\ntest konstruktora macierzy jednostkowej:")

    identity_matrix = Matrix(rows = 3, cols = 3)
    try:
        print(identity_matrix.data)
    except ValueError as e:
        print(e)

    identity_matrix = Matrix([[1, 0], [0, 1]])
    try:
        print(identity_matrix.data)
    except ValueError as e:
        print(e)

    print("\ntest sprawdzajacy rozmiar macierzy:")
    try:
        print(mat1.size())
    except ValueError as e:
        print(e)
    try:
        print(mat2.size())
    except ValueError as e:
        print(e)
    try:
        print(mat3.size())
    except ValueError as e:
        print(e)
    try:
        print(mat4.size())
    except ValueError as e:
        print(e)
    try:
        print(mat5.size())
    except ValueError as e:
        print(e)

    #trace()
    print("\ntrace:")
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

    #determinant()
    print("\ndeterminant()")
    try:
        print(mat1.determinant())
    except ValueError as e:
        print(e)
    try:
        print(mat2.determinant())
    except ValueError as e:
        print(e)
    try:
        print(mat3.determinant())
    except ValueError as e:
        print(e)
    try:
        print(mat4.determinant())
    except ValueError as e:
        print(e)
    try:
        print(mat5.determinant())
    except ValueError as e:
        print(e)
    try:
        print(mat6.determinant())
    except ValueError as e:
        print(e)
    try:
        print(mat7.determinant())
    except ValueError as e:
        print(e)

    #cofactor()
    print("\ncofactor()")
    try:
        print_matrix(mat1.cofactor())
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat2.cofactor())
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat3.cofactor())
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat4.cofactor())
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat5.cofactor())
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat6.cofactor())
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat7.cofactor())
    except ValueError as e:
        print(e)

    #transpose
    print("\ntranspose()")
    print_matrix(mat1.transpose())
    print_matrix(mat2.transpose())
    print_matrix(mat3.transpose())
    print_matrix(mat4.transpose())
    print_matrix(mat5.transpose())
    print_matrix(mat6.transpose())
    print_matrix(mat7.transpose())

    #potęgowanie
    print("\n__pow__()")
    try:
        print_matrix(mat1**2)
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat2**3)
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat3**4)
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat4**2)
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat5 ** 2)
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat6**2)
    except ValueError as e:
        print(e)
    try:
        print_matrix(mat7 ** 2)
    except ValueError as e:
        print(e)

    print("\ntest dodawania macierzy:")
    try:
        add_matrix_result1 = mat1 + mat2
    except ValueError as e:
        print(e)
    try:
        add_matrix_result1 = mat3 + mat4
        print(add_matrix_result1.data)
    except ValueError as e:
        print(e)
    try:
        add_matrix_result1 = mat2 + mat5
        print(add_matrix_result1.data)
    except ValueError as e:
        print(e)
    try:
        add_matrix_result1 = mat2 + mat2
        print(add_matrix_result1.data)
    except ValueError as e:
        print(e)
    try:
        add_matrix_result1 = mat5 + mat5
        print(add_matrix_result1.data)
    except ValueError as e:
        print(e)
    try:
        add_matrix_result1 = mat7 + mat7
        print(add_matrix_result1.data)
    except ValueError as e:
        print(e)


