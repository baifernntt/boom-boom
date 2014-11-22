import pygame
from pygame.locals import *
from memory import SimpleGame

class Memory(SimpleGame):

	def init(self):
	 	super(Memory,self).init()

	def __init__(self):
	 	super(Memory,self).__init__('Memory Matrix')

def main():
	game = Memory()
	game.run()

if __name__ == '__main__':
	main()



