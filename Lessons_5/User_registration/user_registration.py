class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    # Строка документирования, которая будет содержать описание класса (вывод документации: User.__doc__)
    """
    Класс пользователя, содержащий атрибуты: username, password
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    user = User(int('Придумайте логин: '), int('Придумайте пароль: '), int('Повторите ввод пароля для проверки: '))
    database.add_user(user.username, user.password)