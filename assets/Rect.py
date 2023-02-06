import pygame
from game.settings import*

class Page:
    def __init__(self, top, left, width, height, rgb = (0, 0, 0)):
        self.rgb = rgb
        self.width = width
        self.height = height
        self.draw = pygame.draw.rect(SCREEN, self.rgb, pygame.Rect(top, left, self.width, self.height))

    def collision(self, x, y):
        return self.draw.collidepoint((x, y))