import pygame


class Ship():
    def __init__(self, ai_game):
        '''Инициализирует корабль и задает его начальное положение'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.moving_right = False
        self.moving_left = False

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images\ship4.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        '''Обновляем позицию коробля с учётом флага'''
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        '''Рисует корабль в новой позиции'''
        self.screen.blit(self.image, self.rect)
