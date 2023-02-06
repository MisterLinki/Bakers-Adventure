import pygame
import os

class Image(pygame.sprite.Sprite):
	def __init__(self, image:str, size):
		self.image_path = os.path.join(os.path.dirname(f"{os.path.realpath(__file__)}"), f"image\\{image}")	# entrer les noms d'images ( + extension) du sprite		
		self.load = pygame.transform.scale(pygame.image.load(self.image_path).convert_alpha(), size)

	def get_collision(self, x, y):
		return self.load.get_rect().collidepoint(x, y)

