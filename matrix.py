#klasa  Matrix :)
from typing import Union
import numpy as np
from sympy import Matrix as SymMatrix
import copy
from enum import Enum


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

    def __mul__(self, other: Union[Matrix, float, int]) -> Matrix:
        # Mnożenie przez skalar
        if isinstance(other, (float, int)):
            rows, cols = self.size()
            result_data = [
                [self.__matrix[i][j] * other for j in range(cols)]
                for i in range(rows)
            ]
            return Matrix(result_data)
        elif isinstance(other, Matrix):
            # Mnożenie przez macierz
            if self.is_it_ok_to_multiply(other):
                result = np.array(self.__matrix) @ np.array(other.__matrix)
                return Matrix(_matrix = result.tolist())
            else:
                raise ValueError("Niezgodne wymiary do mnożenia macierzy.")

    def __pow__(self, n: int, method = PowMethod.MULTIPLY) -> "Matrix":
        if len(self.__matrix[0]) != len(self.__matrix):
            raise ValueError("Niezgodne wymiary macierzy")

        if n < 0:
            inverse_mat = self.inverse()
            return inverse_mat.__pow__(-n, method)

        if method == PowMethod.MULTIPLY:
            result = Matrix(rows=len(self.__matrix), cols=len(self.__matrix))
            for k in range(n):
                result = result * self
            return result

        if method == PowMethod.JORDAN:
            j_mat, pinv_mat = jordan(self) #co z jordanem????

            sym_j = SymMatrix(j_mat._Matrix__matrix)

            sym_j_pow = sym_j ** n

            j_pow = Matrix(sym_j_pow.tolist())

            p_mat = pinv_mat ** (-1)

            return p_mat * j_pow * pinv_mat

    def size(self) -> tuple[int, int]:
        rows = len(self.__matrix)
        cols = len(self.__matrix[0]) if rows > 0 else 0
        return rows, cols

    def determinant(self) -> float:
        rows, cols = self.size()

    if rows != cols:
        raise ValueError("Wyznacznik jest zdefiniowany tylko dla macierzy kwadratowych.")

    if rows == 0:
        raise ValueError("Nie można obliczyć wyznacznika pustej macierzy.")

    mat = copy.deepcopy(self.__matrix)
    det = 1.0

    for i in range(rows):
        pivot = i

        for r in range(i + 1, rows):
            if abs(mat[r][i]) > abs(mat[pivot][i]):
                pivot = r

        if abs(mat[pivot][i]) < 1e-12:
            return 0.0

        if pivot != i:
            mat[i], mat[pivot] = mat[pivot], mat[i]
            det *= -1

        pivot_value = mat[i][i]
        det *= pivot_value

        for r in range(i + 1, rows):
            factor = mat[r][i] / pivot_value

            for c in range(i + 1, cols):
                mat[r][c] -= factor * mat[i][c]

    return det

    def trace(self) -> float:
        rows, cols = self.size()
        if rows != cols:
            raise ValueError("Ślad jest definiowany tylko dla macierzy kwadratowych.")
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
                minor_det = self.determinant(minor) if minor else 1.0 #brak metody determinant
                cofactor_row.append(((-1) ** (i + j)) * minor_det)
            cofactor_data.append(cofactor_row)
        return Matrix(cofactor_data)

    def inverse(self):
        if len(self.__matrix[0]) != len(self.__matrix):
            raise ValueError("Niezgodne wymiary macierzy")
        if abs(self.determinant()) < 1e-12:
            raise ValueError("Macierz ma zerowy wyznacznik")
        np_mat = np.array(self.__matrix)
        inv = np.linalg.inv(np_mat)
        return Matrix(inv.tolist())

    def is_it_ok_to_multiply(self, matrix2) -> bool:
        row1, col1 = self.size()
        row2, col2 = matrix2.size()
        return col1 == row2

    @staticmethod
    def have_same_size(a: Matrix, b: Matrix) -> bool:
        return a.size() == b.size()

