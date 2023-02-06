import pygame

from assets.image import*
from assets.music import*
from assets.Rect import*

from game.settings import*

def initialisation():
    pygame.init()                           #allumer pygame
    pygame.mixer.init()                     #allumer l'audio de pygame
    Music("musique_2019.mp3", SOUND, True)


def runcursor():
    pygame.mouse.set_visible(False)
    X_AXIS_POS, Y_AXIS_POS = pygame.mouse.get_pos()
    x, y = X_AXIS_POS, Y_AXIS_POS   
    
    return x, y

def information(X_AXIS, Y_AXIS, Clock):
    information = Text(X_AXIS, Y_AXIS).render(f"Screen Size: {X_AXIS}/{Y_AXIS}  FPS: {round(Clock.get_fps())}", False, (255, 255, 255))
    SCREEN.blit(information, (X_AXIS//1.6, 5))  