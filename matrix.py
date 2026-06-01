#klasa  Matrix :)

import numpy as np
from sympy import Matrix as SymMatrix
import copy
from enum import Enum

class PowMethod(Enum):
    MULTIPLY = "MULTIPLY"
    JORDAN = "JORDAN"

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

    def is_it_ok_to_multiply(self, matrix2) -> bool:
        return len(self.__matrix[0]) == len(matrix2.__matrix) #dostosować nazwę pola matrix

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.is_it_ok_to_multiply(other):
                result = np.array(self.__matrix) @ np.array(other.__matrix)
                return Matrix(_matrix = result.tolist())
            else:
                raise ValueError("Niezgodne wymiary macierzy")

    def __pow__(self, n: int, method = PowMethod.MULTIPLY) -> "Matrix":
        if len(self.__matrix[0]) != len(self.__matrix):
            raise ValueError("Niezgodne wymiary macierzy")

        if n < 0:
            inverse_mat = inverse(self) #funkcja inverse do zaimplementowania
            return inverse_mat.__pow__(-n, method)

        if method == PowMethod.MULTIPLY:
            result = Matrix([[1.0 if i == j else 0.0 for j in range(len(self.__matrix[0]))] for i in range(len(self.__matrix))])
            for k in range(n):
                result = result * self
            return result

        if method == PowMethod.JORDAN:
            if method == PowMethod.JORDAN:
                j_mat, pinv_mat = jordan(self)

                sym_j = SymMatrix(j_mat._Matrix__matrix)

                sym_j_pow = sym_j ** n

                j_pow = Matrix(sym_j_pow.tolist())

                p_mat = pinv_mat ** (-1)

                return p_mat * j_pow * pinv_mat

    def trace(self) -> float:
        rows, cols = self.size()    #metoda size jest jeszcze do stworzenia prawdopodobnie przez Rolanda
        if rows != cols:
            raise ValueError("Ślad jest definiowany tylko dla macierzy kwadratowych.")
        return sum(self.__matrix[i][i] for i in range(rows))

    def rank(self) -> int:
        mat = copy.deepcopy(self.__matrix)
        rows, cols = self.size() #metoda size jest jeszcze do stworzenia prawdopodobnie przez Rolanda
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


