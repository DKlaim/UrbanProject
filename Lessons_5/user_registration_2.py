class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    # Строка ниже - строка документирования, которая содержит описание класса (вывод документации: User.__doc__)
    """
    Класс пользователя, содержащий атрибуты username и password, а также отвечает за регистрацию и авторизацию
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    def __getitem__(self, data):
        self.data = data

    @staticmethod
    def registration():
        print('Регистрация пользователя')
        while True:
            user = User(input('Придумайте логин: '), password := input('Придумайте пароль: '),
                        password_confirm := input('Для подтверждения повторите ввод пароля: '))
            if password != password_confirm:
                print()
                print('Ошибка при повторном введении пароля! Попробуйте ещё раз.')
                continue
            else:
                database.add_user(user.username, user.password)
                print()
                print(f'Пользователь {user.username} успешно создан.')
                print()
                break

    def authorization(self):
        print('Авторизация пользователя:')
        while True:
            username = input('Введите логин: ')
            if username and username in self.data:
                password = input('Введите пароль: ')
                if password == self.data[username]:
                    print()
                    print(f'Авторизация пользователя {username} успешно выполнена.')
                    break
                else:
                    print()
                    print('Неверный пароль! Попробуйте ещё раз.')
                    continue
            elif username == '':
                break
            else:
                print()
                print(f'Пользователь {username} не найден. Попробуйте ещё раз или нажмите "Enter" для выхода.')
                continue


if __name__ == '__main__':
    database = Database()
    User.registration()
    User.authorization(database)
