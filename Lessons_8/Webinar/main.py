class InsufficientFundsError(Exception):
    """ Исключение для обработки недостатка средств на счёте. """

    def __init__(self, message='Недостаточно средств на счёте для выполнения операции.'):
        self.message = message
        super().__init__(self.message)


class AccountNotFoundError(Exception):
    """ Исключение для обработки случая, когда счёт не найден. """

    def __init__(self, message='Счёт не найден. Проверьте номер счёта и попробуйте снова.'):
        self.message = message
        super().__init__(self.message)


class InvalidAmountError(Exception):
    """ Исключение для обработки случая, когда введена неверная сумма. """

    def __init__(self, message='Введена неверная сумма. Сумма должна быть положительным числом.'):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    """ Класс для представления банковского счёта. """

    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError('Сумма пополнения должна быть положительным числом.')
        self.balance += amount
        print(f'Депозит успешно пополнен. Текущий баланс: {self.balance:.2f}')

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError('Сумма снятия должна быть положительным числом.')
        if self.balance < amount:
            raise InsufficientFundsError('Недостаточно средств для выполнения операции.')
        self.balance -= amount
        print(f'Снятие успешно выполнено. Текущий баланс: {self.balance:.2f}')

    def get_balance(self):
        return self.balance


class Bank:
    """ Класс для управления несколькими банковскими счетами. """

    def __init__(self):
        self.accounts = {}  # Инициализация словаря для хранения счетов

    def create_account(self, account_number, owner, initial_balance=0.0):
        if account_number in self.accounts:
            raise ValueError('Счёт с таким номером уже существует.')
        new_account = BankAccount(account_number, owner, initial_balance)
        self.accounts[account_number] = new_account
        print(f'Счёт успешно создан для {owner} с номером {account_number} и начальным балансом {initial_balance}')

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError('Счёт с таким номером не найден.')
        return self.accounts[account_number]

    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        account.withdraw(amount)


# Пример использования системы банка
bank = Bank()
# Создание счёта
try:
    bank.create_account('123456', 'Иван Иванов', 1000)
    bank.create_account('654321', 'Петр Петров', 800)
except ValueError as ve:
    print(ve)

# Пополнение счёта
try:
    bank.deposit_to_account('123456', 200)
except (AccountNotFoundError, InvalidAmountError) as e:
    print(e)

# Снятие средств
try:
    bank.withdraw_from_account('123456', 500)
    bank.withdraw_from_account('123456', 5000)
except (AccountNotFoundError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)

# Проверка баланса
try:
    account = bank.get_account('123456')
    print(f'Баланс счёта {account.account_number}: {account.get_balance():.2f}')
except AccountNotFoundError as e:
    print(e)

# Попытка снять деньги с несуществующего счёта
try:
    bank.withdraw_from_account('12345', 100)
except (AccountNotFoundError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)
