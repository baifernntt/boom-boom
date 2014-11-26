import pygame, pygame.mixer
import memory
from pygame.locals import *
from ball import Ball,Blueball
#from score import score

class Memory(memory.SimpleGame):
	BLACK = pygame.Color('black')
	WHITE = pygame.Color('white')
	RED = pygame.Color('red')
	BLUE = pygame.Color('blue')
	bg = pygame.image.load('bg.jpg')
	pygame.mixer.pre_init(48000, -16, 2, 4096)

	def init(self):
	 	super(Memory,self).init()
		global sound
		sound = pygame.mixer.Sound('pon.wav')

	def __init__(self):
		global note,note1
#		score = score()
	 	super(Memory,self).__init__('Boom boom',Memory.bg)
		note = [Ball(480),Ball(300),Ball(410),Ball(480)]
		note1 = [Blueball(470),Blueball(330),Blueball(400),Blueball(450)]
	#	self.redball = Ball(radius=28, pos=(480,139) ,color=Memory.RED)
	#	self.blueball = Ball(radius=28,pos=(480,239),color=Memory.BLUE)

	def render(self,surface):
		pygame.draw.circle(surface, pygame.Color('black'),(100,139),2,0)
		pygame.draw.circle(surface, pygame.Color('black'),(47,139),2,0)
		sound.play()
		for balls in note:
			balls.render(surface)
		for blueballs in note1:
			blueballs.render(surface)
	
	def update(self):
		for balls in note:
			if balls.isCollide():
				print balls.x , balls.x+balls.radius*2
				if pygame.key.get_pressed()[K_SPACE]:
					balls.delete()
				print "collide"

			balls.update()
#			score.update(balls)
		for blueballs in note1:
			if blueballs.isCollide():
				if pygame.key.get_pressed()[K_b]:
					blueballs.delete()

			blueballs.update()
def main():
	game = Memory()
	game.run()

if __name__ == '__main__':
	main()



