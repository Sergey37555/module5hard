class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for users in self.users:
            if nickname == users.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_users = User(nickname, password, age)
        self.users.append(new_users)
        self.current_user = new_users

    def log_in(self, nickname, password):
        for users in self.users:
            if nickname == users.nickname and password == users.password:
                self.current_user = users

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for clip in args:
            if clip not in self.videos:
                self.videos.append(clip)

    def get_videos(self, text):
        list_of_clips = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_of_clips.append(video.title)
        return list_of_clips

    def watch_video(self, movie: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(1, x.duration + 1):
                    print(i, end=' ')
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')


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