import pygame,pygame.mixer
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
	pygame.mixer.pre_init(22050, -16, 1, 12000)

	def init(self):
	 	super(Memory,self).init()
		self.render_score()
		global sound
		#global movie,movie_screen
		#pygame.mixer.quit()
		sound = pygame.mixer.Sound('pon1.ogg')
		#movie = pygame.movie.Movie('pon.mpg')
		#movie_screen = pygame.Surface(movie.get_size()).covert()
		#movie.set_display(movie_screen)

	def __init__(self):
		global note,note1
		self.score =0
	 	super(Memory,self).__init__('Boom boom',Memory.bg)
		note = [Ball(480),Ball(300),Ball(410),Ball(480),Ball(540)]
		note1 = [Blueball(470),Blueball(330),Blueball(400),Blueball(480),Blueball(590)]

	def render_score(self):
		self.score_imgae = self.font.render("Score = %d" %self.score,0,Memory.BLACK)

	def render(self,surface):
		pygame.draw.circle(surface, pygame.Color('black'),(100,139),2,0)
		pygame.draw.circle(surface, pygame.Color('black'),(47,139),2,0)
		surface.blit(self.score_imgae,(10,10))
		#self.surface.blit(movie_screen,(360,40))
		for balls in note:
			balls.render(surface)
		for blueballs in note1:
			blueballs.render(surface)
	
	def update(self):
		for balls in note:
			if balls.isCollide():
				print balls.x , balls.x+balls.radius*2
				if pygame.key.get_pressed()[K_r]:
					self.render_score()
					self.score += 100
					balls.delete()
				print "collide"

			balls.update()
#			score.update(balls)
		for blueballs in note1:
			if blueballs.isCollide():
				if pygame.key.get_pressed()[K_b]:
					self.score += 100
					self.render_score()
					blueballs.delete()

			blueballs.update()
		sound.play()

def main():
	game = Memory()
	game.run()

if __name__ == '__main__':
	main()



