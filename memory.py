from __future__ import annotations
from operation_model import OperationModel
import json

class Memory:
    def __init__(self, size: int = 10):
        self.__memory: list[OperationModel] = []
        self.__max_size: int = size

    def __getitem__(self, key: int) -> OperationModel:
        return self.__memory[key]

    def __setitem__(self, key: int, value: OperationModel) -> None:
        if key >= len(self.__memory):
            raise IndexError("Indeks poza zakresem pamięci.")
        self.__memory[key] = value

    def size(self) -> int:
        return len(self.__memory)

    def addo_op(self, op: OperationModel) -> None:
        if len(self.__memory) >= self.__max_size:
            self.__memory.pop(0)
        self.__memory.append(op)

    def clear(self) -> None:
        self.__memory.clear()

    def to_str_json(self) -> str:
        memory_list = [op.to_dict() for op in self.__memory]
        return json.dumps(memory_list, indent = 4)