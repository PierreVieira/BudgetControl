from model.transaction_type import TransactionType


class Transaction:
    def __init__(self, type: TransactionType, value: float, description: str, day: int):
        self.type = type
        self.value = value
        self.description = description
        self.day = day

    def __str__(self):
        return f'type: {self.type} | value: {self.value} | description: {self.description} | day: {self.day}'

    def __repr__(self):
        return self.__str__()
