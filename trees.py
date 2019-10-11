import pygame
from settings import Settings as gset

class Tree(pygame.sprite.Sprite):

    def __init__(self, screen, turn):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.turn = turn

        self.image = pygame.image.load(gset.tree).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        if self.turn == "left":
            self.rect.left = self.screen_rect.left + 200
        else:
            self.rect.right = self.screen_rect.right - 200
