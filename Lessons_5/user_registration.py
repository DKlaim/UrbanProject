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
    while True:
        user = User(input('Придумайте логин: '), password := input('Придумайте пароль: '),
                    password_confirm := input('Повторите ввод пароля для проверки: '))
        if password != password_confirm:
            print('Ошибка при повторном вводе пароля! Попробуйте ещё раз.')
            continue
        else:
            database.add_user(user.username, user.password)
            print(f'Пользователь {user.username} успешно создан.')
            print(database.data)
            break
