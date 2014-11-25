import pygame
from pygame.locals import *

class Ball(object):
	up_lane = 139
	down_lane = 239
	def __init__(self,lane, x):
		self.x = x
		self.y = 0
		self.color = pygame.Color('Blue')
		if lane==1:
			self.color = pygame.Color('red')
			self.y = Ball.up_lane
		elif lane==2:
			self.color = pygame.Color('blue')
			self.y = Ball.down_lane	
		self.radius = 28

	def render(self,surface):
		self.circle = pygame.draw.circle(surface,self.color,(self.x,self.y), self.radius,0)

	def get_circle(self):
		pass

	def delete(self):
		self.x = 1000

	def update(self):
		self.x -= 5
		
