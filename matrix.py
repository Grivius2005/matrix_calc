#klasa  Matrix :)

class Matrix:

    def is_it_ok_to_multiply(self, matrix2: Matrix) -> bool:
        return len(self.matrix[0]) == len(matrix2.matrix) #dostosować nazwę pola matrix