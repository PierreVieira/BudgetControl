from model.transaction import Transaction
from model.transaction_type import TransactionType


class Transactions:
    def __init__(self, data: list[Transaction]):
        self.__data = data

    def __get_transactions_filtered(self, transaction_type: TransactionType):
        return list(filter(lambda x: x.type == transaction_type, self.__data))

    def __get_by_type(self, transaction_type: TransactionType):
        transactions_filtered = self.__get_transactions_filtered(transaction_type)
        return list(map(lambda transaction: transaction.value, transactions_filtered))

    def __get_sum_by_type(self, transaction_type: TransactionType):
        return sum(self.__get_by_type(transaction_type))

    def __transform_to_values(self, transactions: list[Transaction]):
        return list(map(lambda transaction: transaction.value, transactions))

    def get_gains_value_total(self):
        return self.__get_sum_by_type(TransactionType.GAIN)

    def get_expenses_value_total(self):
        return self.__get_sum_by_type(TransactionType.EXPENSE)

    def get_gains(self):
        return self.__get_transactions_filtered(TransactionType.GAIN)

    def get_expenses(self):
        return self.__get_transactions_filtered(TransactionType.EXPENSE)

    def __get_transactions_by_day(self, day: int, transactions: list[Transaction]):
        return list(filter(lambda transaction: transaction.day == day, transactions))

    def get_expenses_between(self, end):
        expenses = self.get_expenses()
        expenses_filtered = self.__get_transactions_by_day(end, expenses)
        return sum(self.__transform_to_values(expenses_filtered))

    def get_gains_between(self, end):
        gains = self.get_gains()
        gains_filtered = self.__get_transactions_by_day(end, gains)
        return sum(self.__transform_to_values(gains_filtered))

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return self.__str__()
