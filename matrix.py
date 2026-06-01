#klasa  Matrix :)

import numpy as np

class Matrix:
    def __init__(self, rows: int = None, cols: int = None, operated_matrix: list[list[float]] = None):
        if operated_matrix is not None:
            if len(operated_matrix) == 0 or len(operated_matrix[0]) == 0:
                raise ValueError("Provided matrix cannot be empty.")

            self.rows = len(operated_matrix)
            self.cols = len(operated_matrix[0])

            if any(len(row) != self.cols for row in operated_matrix):
                raise ValueError("All rows must have the same number of columns.")

            self.operated_matrix = [[float(val) for val in row] for row in operated_matrix]
        else:
            if rows is None:
                raise ValueError("You must provide either 'operated_matrix' or 'rows'.")

            self.rows = rows
            self.cols = cols if cols is not None else rows

            if self.rows <= 0 or self.cols <= 0:
                raise ValueError("Matrix dimensions must be greater than zero.")

            if self.rows == self.cols:
                self.operated_matrix = [
                    [1.0 if i == j else 0.0 for j in range(self.cols)]
                    for i in range(self.rows)
                ]
            else:
                self.operated_matrix = [
                    [0.0 for _ in range(self.cols)]
                    for _ in range(self.rows)
                ]

    def is_it_ok_to_multiply(self, matrix2) -> bool:
        return len(self.operated_matrix[0]) == len(matrix2.operated_matrix) #dostosować nazwę pola matrix

    def __mul__(self, other):
        if self.is_it_ok_to_multiply(other):
            result = np.array(self.operated_matrix) @ np.array(other.operated_matrix)
            return Matrix(operated_matrix=result.tolist())
        else:
            raise ValueError("Niezgodne wymiary macierzy")

    def which_power_method(self, method: str) -> int:
        methods = {"Jordan": 1, "multiply": 2}
        return methods.get(method) #to nie ma sensu
