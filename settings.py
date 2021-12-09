class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion'''

    def __init__(self):
        '''Инициализация настроек игры'''
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (173, 216, 230)

        self.ship_speed_factor = 1.5