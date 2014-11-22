import pygame
from pygame.locals import *

class SimpleGame(object):

	def __init__(self,title,window_size=(640,480),fps = 60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.is_terminated = False

	def is_terminated(self):
		self.is_terminated = True

	def run(self):
		self.init()
		while True:
			self.update()
			self.render()

	def init(self):
		self.game_init()

	def update(self):
		pass

	def render(self):
		pass

	def game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace",20)
