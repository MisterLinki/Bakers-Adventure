import pygame
import os

class Music:
	def __init__(self, music:str, SOUND, replay = False):

		self.music_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),f"Music\\{music}") # entrer le nom de la musique ( + extension) de la musique 
		self.load = pygame.mixer.music.load(self.music_path)
		self.load = pygame.mixer.music.set_volume(SOUND)

		if replay:  self.load = pygame.mixer.music.play(-1)
		else:   self.load = pygame.mixer.music.play(1)
				
	def get_time(self):
		return pygame.mixer.music.get_pos()
