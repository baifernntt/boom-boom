import pygame
import memory
from pygame.locals import *
from ball import Ball

class Memory(memory.SimpleGame):

	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	RED = pygame.Color('red')
	BLUE = pygame.Color('blue')
	bg = pygame.image.load('bg.jpg')

	def init(self):
	 	super(Memory,self).init()

	def __init__(self):
		global note
	 	super(Memory,self).__init__('Boom boom',Memory.bg)
		note = [Ball(1,260),Ball(2,254),Ball(1,130),Ball(2,480),Ball(1,480),Ball(2,480)]
	#	self.redball = Ball(radius=28, pos=(480,139) ,color=Memory.RED)
	#	self.blueball = Ball(radius=28,pos=(480,239),color=Memory.BLUE)

	def render(self,surface):
		for balls in note:
			balls.render(surface)
	
	def update(self):
		for balls in note:
			balls.update()

def main():
	game = Memory()
	game.run()

if __name__ == '__main__':
	main()



