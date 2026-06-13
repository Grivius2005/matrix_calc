from matrix import Matrix

class OperationModel:
    def __init__(self, op_id: int, matrix1: Matrix, matrix2: Matrix, result: Matrix):
        self.opId: int = op_id
        self.matrix1: Matrix = matrix1
        self.matrix2: Matrix = matrix2
        self.result: Matrix = result

    def to_dict(self) -> dict:
        return {
            "opId": self.opId,
            "matrix1": self.matrix1.data if self.matrix1 else None,
            "matrix2": self.matrix2.data if self.matrix2 else None,
            "result": self.result.data if self.result else None
        }