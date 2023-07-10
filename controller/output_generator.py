from model.transactions import Transactions


class OutputGenerator:
    def __init__(self, transactions: Transactions):
        self.transactions = transactions

    def __show_transaction(self, transaction, percentage):
        print(f'{transaction.description} ({(percentage * 100):.2f} %): R$ {transaction.value:.2f}')

    def __show_transactions(self, transactions):
        total = sum(map(lambda transaction_data: transaction_data.value, transactions))
        for transaction in transactions:
            self.__show_transaction(transaction, transaction.value / total)

    def generate(self):
        expenses = self.transactions.get_expenses()
        gains = self.transactions.get_gains()
        expenses_total = self.transactions.get_expenses_value_total()
        expenses_until_15 = self.transactions.get_expenses_between(15)
        gains_until_15 = self.transactions.get_gains_between(15)
        expenses_after_15 = self.transactions.get_expenses_between(30)
        gains_after_15 = self.transactions.get_gains_between(30)
        gains_total = self.transactions.get_gains_value_total()
        profit_until_15 = gains_until_15 - expenses_until_15
        profit_after_15 = gains_after_15 - expenses_after_15
        print(f'===== GAINS =====')
        self.__show_transactions(gains)
        print(f'\nTotal: R$ {gains_total:.2f}')
        print(f'===== Expenses =====')
        self.__show_transactions(expenses)
        print(f'-------------------')
        print(f'Expenses 01-15: R$ {expenses_until_15:.2f}')
        print(f'Expenses 15-30: R$ {expenses_after_15:.2f}')
        print(f'Total expenses: R$ {expenses_total:.2f}')
        print(f'=' * 15 + '\n')
        print(f'Profit 01-15: R$ {profit_until_15:.2f}')
        print(f'Profit 15-30: R$ {profit_after_15:.2f}')
        print(f'Total profit: R$ {gains_total - expenses_total:.2f}')
