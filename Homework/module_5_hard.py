class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users[nickname] = [password, age]
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        if nickname in self.users and hash(self.users[nickname][0]) == hash(password):
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        pass

    def get_videos(self):
        pass

    def watch_video(self):
        pass


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash((self.nickname, self.password))


if __name__ == '__main__':
    # user = User('den', 123123, 23)
    # print(user)
    # print(hash(user))
    # print(user.age)
    # v1 = Video('Лучший язык программирования 2024 года', 200)
    # v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # print(v1)
    # print(v2)
    ur = UrTube()
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    print(ur.current_user)
    print(hash(ur.current_user))
