#klasa  Matrix :)

class Matrix:

    def is_it_ok_to_multiply(self, matrix2: Matrix) -> bool:
        return len(self.matrix[0]) == len(matrix2.matrix) #dostosować nazwę pola matrix

    def which_power_method(self, method: string) -> int:
        dict = {"Jordan" : 1, "multiply" : 2}
        return dict[method] #to nie ma sensu
