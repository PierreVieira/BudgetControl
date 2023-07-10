import json

from model.transaction import Transaction
from model.transactions import Transactions
from model.transaction_type import TransactionType

EXPENSES_KEY = 'despesas'
GAINS_KEY = 'ganhos'
DESCRIPTION_KEY = "description"
VALUE_KEY = "value"


class JsonParser:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def parse(self):
        with open(self.__file_path) as file:
            data: dict = json.load(file)
        transactions_data = []
        for day, transactions_type in data.items():
            for key, transactions_values in transactions_type.items():
                if key == EXPENSES_KEY:
                    transaction_type = TransactionType.EXPENSE
                else:
                    transaction_type = TransactionType.GAIN
                for transaction in transactions_values:
                    transactions_data.append(
                        Transaction(transaction_type, transaction[VALUE_KEY], transaction[DESCRIPTION_KEY], int(day))
                    )
        return Transactions(transactions_data)
