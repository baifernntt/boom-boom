import pygame
from pygame.locals import *

class SimpleGame(object):

	def __init__(self,title,background,window_size=(640,480),fps = 60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.is_terminated = False
		self.background = background

	def terminated(self):
		self.is_terminated = True

	def run(self):
		self.init()
		while not self.is_terminated:
			self.__handle_events()
			self.update()
			self.surface.blit(self.background,[0,0])
			self.render(self.surface)
			pygame.display.update()

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()

	def init(self):
		self.game_init()

	def update(self):
		pass

	def render(self,surface):
		pass

	def game_init(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.surface = pygame.display.set_mode(self.window_size)
		pygame.display.set_caption(self.title)
		self.font = pygame.font.SysFont("monospace",20)
