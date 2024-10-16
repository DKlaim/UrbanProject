class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if self.users:
            list_usernames = []
            for user in self.users:
                list_usernames += user
            if nickname in list_usernames:
                print(f'Пользователь {nickname} уже существует')
            else:
                self.users += [{nickname: [password, age]}]
                self.log_in(nickname, password)
        else:
            self.users += [{nickname: [password, age]}]
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname in user and hash(user[nickname][0]) == hash(password):
                self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        self.videos += other

    def get_videos(self, word):
        video_list = []
        word = word.lower
        for video in self.users:
            for title in video:
                title = title.lower
                if word in title:
                    video_list += self.videos[0][0]
        return video_list



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

    def __repr__(self):
        return f'{self.title}, {self.duration})'


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
    ur = UrTube()

    # user1 = User('den', 123123, 23)
    # user2 = User('max', 321123, 22)
    #
    # print(user1)
    # print(hash(user1))
    # print(user1.age)
    # ur.register('den', 123123, 23)
    # print()
    #
    # print(user2)
    # print(hash(user2))
    # print(user2.age)
    # ur.register('max', 321123, 22)
    # print()
    #
    # ur.register('den', 123123, 23)
    # print()
    #
    # ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    # print(ur.current_user)
    # print(hash(ur.current_user))
    #
    # print(ur.users)
    # print()

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    print(v1)
    print(v2)
    print()

    ur.add(v1, v2)
    print(ur.videos)

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
