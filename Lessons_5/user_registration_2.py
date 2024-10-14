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

        def answer_for_emptiness():
            print('----------------------------------------------')
            print('Поле не может быть пустым! Попробуйте ещё раз.')
            print('----------------------------------------------')

        print('Регистрация пользователя')
        while True:
            login = input('Придумайте логин: ')
            if login:
                password = input('Придумайте пароль: ')
                if password:
                    password_confirm = input('Для подтверждения повторите ввод пароля: ')
                    if password_confirm:
                        if password == password_confirm:
                            user = User(login, password, password_confirm)
                            database.add_user(user.username, user.password)
                            print('----------------------------------------------')
                            print(f'Пользователь {user.username} успешно создан.')
                            print('----------------------------------------------')
                            break
                        else:
                            print('---------------------------------------------------------')
                            print('Ошибка при повторном введении пароля! Попробуйте ещё раз.')
                            print('---------------------------------------------------------')
                            continue
                    else:
                        answer_for_emptiness()
                        continue
                else:
                    answer_for_emptiness()
                    continue
            else:
                answer_for_emptiness()
                continue

    def authorization(self):
        print('Авторизация пользователя')
        while True:
            username = input('Введите логин: ')
            if username and username in self.data:
                password = input('Введите пароль: ')
                if password == self.data[username]:
                    print('----------------------------------------------')
                    print(f'Авторизация пользователя {username} успешно выполнена.')
                    print('----------------------------------------------')
                    break
                else:
                    print('----------------------------------------------')
                    print('Неверный пароль! Попробуйте ещё раз.')
                    print('----------------------------------------------')
                    continue
            elif username == '':
                break
            else:
                print('--------------------------------------------------')
                print(f'Пользователь {username} не найден.\nПопробуйте ещё раз или нажмите "Enter" для выхода.')
                print('--------------------------------------------------')
                continue


if __name__ == '__main__':
    database = Database()
    User.registration()
    User.authorization(database)
