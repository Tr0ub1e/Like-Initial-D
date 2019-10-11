import pygame
import os
from settings import Settings as gset


class Car():

    def __init__(self, screen):

        self.screen = screen
        self.surf = pygame.image.load(gset.up_image).convert()
        self.screen_rect = screen.get_rect()
        self.rect = self.surf.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 200

        self.up = pygame.image.load(gset.up_image).convert_alpha()
        self.right = pygame.image.load(gset.right_image).convert_alpha()
        self.left = pygame.image.load(gset.left_image).convert_alpha()


    def blitme(self):

        self.screen.blit(self.surf, self.rect)


    def update(self, direction, debug):

        if direction == "left" and self.rect.x > self.screen_rect.left + 300:
            self.rect.x -= 15
            self.surf = self.left
#1603
        if direction == "right" and self.rect.x < self.screen_rect.right - 300:
            self.rect.x += 15
            self.surf = self.right

        if direction == None:
            self.surf = self.up

        if debug == True:
            print("car x {}, car y {} \n screen_height ".format(self.rect.x, self.rect.y))
