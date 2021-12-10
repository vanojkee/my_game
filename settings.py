class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion'''

    def __init__(self):
        '''Инициализация настроек игры'''
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (0, 0, 0)

        # Скорость передвежения корабля
        self.ship_speed_factor = 0.5

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

