#klasa Memory :)

class Memory:
    def __init__(self, size: int):
        self.__memory: list[OperationModel] = []
        self.__max_size: int = size
