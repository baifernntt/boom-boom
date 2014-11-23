import pygame
import memory
from pygame.locals import *

class Memory(memory.SimpleGame):

	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	bg = pygame.image.load('bg.jpg')

	def init(self):
	 	super(Memory,self).init()

	def __init__(self):
	 	super(Memory,self).__init__('Boom boom',Memory.bg)

def main():
	game = Memory()
	game.run()

if __name__ == '__main__':
	main()



