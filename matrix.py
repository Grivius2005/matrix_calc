#klasa  Matrix :)

import numpy as np
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

    def is_it_ok_to_multiply(self, matrix2) -> bool:
        return len(self.__matrix[0]) == len(matrix2.operated_matrix) #dostosować nazwę pola matrix

    def __mul__(self, other):
        if self.is_it_ok_to_multiply(other):
            result = np.array(self.__matrix) @ np.array(other.operated_matrix)
            return Matrix(_matrix = result.tolist())
        else:
            raise ValueError("Niezgodne wymiary macierzy")

    def trace(self) -> float:
        rows, cols = self.size()    #metoda size jest jeszcze do stworzenia prawdopodobnie przez Rolanda
        if rows != cols:
            raise ValueError("Ślad jest definiowany tylko dla macierzy kwadratowych.")
        return sum(self.__matrix[i][i] for i in range(rows))

    def which_power_method(self, method: str) -> int:
        methods = {"Jordan": 1, "multiply": 2}
        return methods.get(method) #to nie ma sensu
