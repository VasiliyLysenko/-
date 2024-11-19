from time import sleep


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, login, password):
        l_login = login
        l_password = hash(password)
        for i in self.users:
            if i.nickname == l_login and i.password == l_password:
                self.current_user = i
                return self.current_user

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == i.nickname:
                return print(f'Пользователь {nickname} уже существует')
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)

    def get_videos(self, key_word):
        kw = key_word.lower()
        v_list = []
        for i in self.videos:
            if kw in i.title.lower():
                v_list.append(i.title)
        return v_list

    def watch_video(self, video_title):
        if not self.current_user:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        for i in self.videos:
            if video_title == str(i):
                if bool(i) and int(self.current_user) < 18:
                    return print('Вам нет 18 лет, пожалуйста покиньте страницу')
                for k in range(i.time_now, len(i)):
                    i.time_now += 1
                    print(i.time_now)
                    sleep(1)
                i.time_now = 0
                print('Конец видео')
                return


class Video:
    def __init__(self, title, duration, t_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = t_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __len__(self):
        return self.duration

    def __bool__(self):
        return self.adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

    def __int__(self):
        return self.age


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