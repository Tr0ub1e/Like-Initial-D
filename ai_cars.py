import pygame
from settings import Settings as gset
from random import randint

class Ai_cars(pygame.sprite.Sprite):

    def __init__(self, screen, image):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = image

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # spawn car
        self.rect.x = randint(self.screen_rect.left + 300, self.screen_rect.right - 300)
