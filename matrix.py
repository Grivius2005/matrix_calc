# klasa  Matrix :)
from __future__ import annotations
from typing import Union
import json
import copy


class Matrix:
    def __init__(self, _matrix: list[list[float]] = None, rows: int = None, cols: int = None):
        if _matrix is not None:
            self.__matrix: list[list[float]] = copy.deepcopy(_matrix)
        elif rows is not None and cols is not None:
            if rows <= 0 or cols <= 0:
                raise ValueError("Liczba wierszy i kolumn musi być większa od zera.")
            if rows == cols:
                self.__matrix = [
                    [1.0 if i == j else 0.0 for j in range(cols)]
                    for i in range(rows)
                ]
            else:
                self.__matrix = [
                    [0.0 for _ in range(cols)]
                    for _ in range(rows)
                ]

        else:
            self.__matrix = []

    @property
    def data(self) -> list[list[float]]:
        return self.__matrix


    def __eq__(self, matrix2: Matrix) -> bool:
        if not Matrix.have_same_size(self, matrix2):
            return False
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                if abs(self.__matrix[i][j] - matrix2.data[i][j]) > 1e-9:
                    return False
        return True


    def __add__(self, matrix2: Matrix) -> Matrix:
        if not Matrix.have_same_size(self, matrix2):
            raise ValueError("Macierze muszą mieć te same wymiary, aby je dodać.")
        rows, cols = self.size()
        result_data = [
            [self.__matrix[i][j] + matrix2.__matrix[i][j] for j in range(cols)]
            for i in range(rows)
        ]
        return Matrix(result_data)

    def __sub__(self, matrix2: Matrix) -> Matrix:
        if not Matrix.have_same_size(self, matrix2):
            raise ValueError("Macierze muszą mieć te same wymiary, aby je odjąć.")
        rows, cols = self.size()
        result_data = [
            [self.__matrix[i][j] - matrix2.__matrix[i][j] for j in range(cols)]
            for i in range(rows)
        ]
        return Matrix(result_data)

    def is_it_ok_to_multiply(self, matrix2) -> bool:
        row1, col1 = self.size()
        row2, col2 = matrix2.size()
        # warunek mnorzenia Macierzy
        return col1 == row2

    def __mul__(self, other: Union[Matrix, float, int]) -> Matrix:
        if isinstance(other, (float, int)):
            result_data = [[val * other for val in row] for row in self.__matrix]
            return Matrix(_matrix = result_data)
        elif isinstance(other, Matrix):
            if not Matrix.can_be_multiplied(self, other):
                raise ValueError("Niezgodne wymiary do mnożenia macierzy.")

            rows_a, cols_a = self.size()
            rows_b, cols_b = other.size()

            result_data = [[0.0] * cols_b for _ in range(rows_a)]
            for i in range(rows_a):
                for j in range(cols_b):
                    for k in range(cols_a):
                        result_data[i][j] += self.__matrix[i][k] * other.data[k][j]
            return Matrix(_matrix = result_data)
        else:
            raise TypeError("Mnożenie obsługiwane tylko dla typu Matrix, float lub int.")

    def __pow__(self, k: int) -> Matrix:
        rows, cols = self.size()
        if rows != cols:
            raise ValueError("Potęgowanie jest możliwe tylko dla macierzy kwadratowych.")
        if k < 0:
            raise ValueError("Obsługiwane są tylko nieujemne potęgi.")

        result = Matrix(rows=rows, cols=cols)
        base = Matrix(_matrix = self.__matrix)

        for _ in range(k):
            result = result * base
        return result

    def size(self) -> tuple[int, int]:
        rows = len(self.__matrix)
        cols = len(self.__matrix[0]) if rows > 0 else 0
        return rows, cols

    def _calc_det(self, matrix_data: list[list[float]]) -> float:
        mat = copy.deepcopy(matrix_data)
        n = len(mat)

        det = 1.0
        for i in range(n):
            if mat[i][i] == 0:
                for j in range(i + 1, n):
                    if mat[j][i] != 0:
                        mat[i], mat[j] = mat[j], mat[i]
                        det *= -1.0
                        break
                else:
                    return 0.0

            det *= mat[i][i]
            for j in range(i + 1, n):
                factor = mat[j][i] / mat[i][i]
                for k in range(i, n):
                    mat[j][k] -= factor * mat[i][k]
        return det

    def determinant(self) -> float:
        """Oblicza wyznacznik jednym domyślnym sposobem (Eliminacja Gaussa)."""
        rows, cols = self.size()
        if rows != cols or rows == 0:
            raise ValueError("Wyznacznik można obliczyć tylko dla niepustych macierzy kwadratowych.")
        return self._calc_det(self.__matrix)

    def trace(self) -> float:
        rows, cols = self.size()
        # sprawdzenie czy macierz jest kwadratowa
        if rows != cols:
            raise ValueError("Ślad jest definiowany tylko dla macierzy kwadratowych.")
        # zwraca sumę elementów na głównej przekątnej
        return sum(self.__matrix[i][i] for i in range(rows))

    def rank(self) -> int:
        mat = copy.deepcopy(self.__matrix)
        rows, cols = self.size()
        r = 0
        for c in range(cols):
            if r >= rows:
                break
            pivot = r
            while pivot < rows and abs(mat[pivot][c]) < 1e-9:
                pivot += 1

            if pivot < rows:
                mat[r], mat[pivot] = mat[pivot], mat[r]
                for i in range(r + 1, rows):
                    factor = mat[i][c] / mat[r][c]
                    for j in range(c, cols):
                        mat[i][j] -= factor * mat[r][j]
                r += 1
        return r

    def transpose(self) -> "Matrix":
        rows, cols = self.size()
        transposed_data = [[self.__matrix[j][i] for j in range(rows)] for i in range(cols)]
        return Matrix(transposed_data)

    def cofactor(self) -> "Matrix":
        rows, cols = self.size()
        if rows != cols:
            raise ValueError("Macierz dopełnień istnieje tylko dla macierzy kwadratowych.")

        cofactor_data = []
        for i in range(rows):
            cofactor_row = []
            for j in range(cols):
                minor = [r[:j] + r[j + 1:] for idx, r in enumerate(self.__matrix) if idx != i]
                minor_det = self._calc_det(minor) if minor else 1.0  # brak metody determinant
                cofactor_row.append(((-1) ** (i + j)) * minor_det)
            cofactor_data.append(cofactor_row)
        return Matrix(cofactor_data)

    def jordan(self) -> tuple[Matrix, Matrix, Matrix]:
        from sympy import Matrix as SymMatrix

        sym_mat = SymMatrix(self.__matrix)
        p_sym, j_sym = sym_mat.jordan_form()
        p_inv_sym = p_sym.inv()

        def to_float_list(s_mat):
            return [[float(complex(val).real) for val in row] for row in s_mat.tolist()]

        p = Matrix(_matrix = to_float_list(p_sym))
        j = Matrix(_matrix =to_float_list(j_sym))
        p_inv = Matrix(_matrix=to_float_list(p_inv_sym))

        return p, j, p_inv

    @staticmethod
    def have_same_size(a: Matrix, b: Matrix) -> bool:
        return a.size() == b.size()

    @staticmethod
    def can_be_multiplied(a: Matrix, b: Matrix) -> bool:
        return a.size()[1] == b.size()[0]
