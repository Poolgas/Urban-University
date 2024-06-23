from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __eq__(self, other):
        if isinstance(User, other):
            return self.password == other.password
        return False

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def register(self, nickname, password, age):
        user = User(nickname, hash(password), age)
        if user.nickname not in self.users.keys():
            self.users[user.nickname] = [user.password, user.age]
            self.log_in(nickname, hash(password))
        else:
            print('Пользователь {} уже существует'.format(nickname))

    def log_in(self, login, password):
        if login in self.users.keys() and self.users[login][0] == hash(password):
            self.current_user = login
        else:
            print('Не правельный пароль', self.users[login][0])
    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            if isinstance(arg, Video):
                if arg.title not in self.videos:
                    self.videos[arg.title] = arg.duration, arg.time_now, arg.adult_mode

    def get_videos(self, s_word):
        video_list = []
        for key in self.videos.keys():
            if s_word.lower() in key.lower():
                video_list.append(key)
        return video_list
    def watch_videos(self, name_video):
        if self.current_user is not None:
            if self.videos[name_video][2] is True and self.users[self.current_user][1] <=18:
                print('Вам не 18 лет, пожалуйста покиньте страницу')
                self.log_out()
            else:
                for i in range (1, self.videos[name_video][0] + 1):
                    print(i, end = ' ')
                print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_videos('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_videos('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_videos('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_videos('Лучший язык программирования 2024 года!')
