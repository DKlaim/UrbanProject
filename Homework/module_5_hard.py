class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if not self.users:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            for user in self.users:
                if nickname == user.nickname:
                    print(f'Пользователь {nickname} уже существует')
                    break
                else:
                    self.users.append(User(nickname, password, age))
                    self.log_in(nickname, password)
                    break

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname in user and hash(user.password) == hash(password):
                self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        if other not in self.videos:
            self.videos += other
        return self.videos

    def get_videos(self, word):
        video_list = []
        for video in self.videos:
            if word in video and video not in video_list:
                video_list.append(video)
        return video_list

    def watch_video(self, title_video):
        from time import sleep

        if self.current_user:
            for user in self.users:
                if f'{self.current_user}' in user:
                    for video in self.videos:
                        if title_video == video.title:
                            if video.adult_mode and user.age >= 18:
                                for i in range(1, video.duration + 1):
                                    print(i)
                                    sleep(1)
                                print('Конец видео')
                            else:
                                print('Вам нет 18 лет, пожалуйста покиньте страницу.')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео.')


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'

    def __contains__(self, item):
        return item.lower() in self.title.lower()


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash((self.nickname, self.password))

    def __contains__(self, item):
        return item in self.nickname


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
