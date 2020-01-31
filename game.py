import pygame
import resources as rs

import itertools
import time
import math

DISPLAY_WINDOW_X , DISPLAY_WINDOW_Y = (500,500)
DISPLAY_WINDOW = (DISPLAY_WINDOW_X,DISPLAY_WINDOW_Y)

BLACK = (0,0,0)

class Background:
	def __init__(self,screen):
		self.screen = screen
		self.img    = rs.grass

		#Calucalte minimum buffer surface size
		if self.img.get_width() > screen.get_width() or self.img.get_height() > screen.get_height():
			raise Exception('Check your sprite size, it shouldnt exceed screen shapes')
		self.surface_w = int(math.ceil(screen.get_width()*2/self.img.get_width()))*self.img.get_width()
		self.surface_h = int(math.ceil(screen.get_height()*2/self.img.get_height()))*self.img.get_height()

		#Creating a new surface with tiled screen for smooth movement between co-ordinates
		self.surface = pygame.Surface((self.surface_w, self.surface_h))
		
		gw , gh = self.img.get_width() , self.img.get_height()
		for x,y in itertools.product(range(0,self.surface_w+1,gw),
									 range(0,self.surface_h+1,gh)):
			#print(x,y)
			self.surface.blit(self.img,(x,y))

		#Current bg coords
		self.curr_X = 0
		self.curr_Y = 0

		print('Bg W:',self.surface_w,'Bg H:',self.surface_h)

	def draw(self,a=0,b=0):

		#Update of the surface co-ords
		self.curr_X = (self.curr_X + a) % (self.surface_w // 2)
		self.curr_Y = (self.curr_Y + b) % (self.surface_h // 2)

		# Basic fill, Not required if confident that will not loose the surface.
		self.screen.fill(BLACK)
		
		# Cropped image from surface
		self.screen.blit(self.surface,(0,0),(self.curr_X,self.curr_Y,self.screen.get_width(),self.screen.get_height()))

class Player(pygame.sprite.Sprite):
	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.img    = rs.player['animation']

		self.curr = 0
		self.prev_key = 'up'

	def draw(self, key):
		if key == None:
			self.curr = 0
			key = self.prev_key
		self.curr = (self.curr + 1) % len(self.img[key])
		self.screen.blit(self.img[key][self.curr],(self.screen.get_width()//2-self.img[key][self.curr].get_width()//2,self.screen.get_height()//2-self.img[key][self.curr].get_height()//2))
		self.prev_key = key
		#print(self.curr)

def main():

	#Game init
	pygame.init()
	'''
	Not required as of now.
		# load and set the logo
		#logo = pygame.image.load("logo32x32.png")
		#pygame.display.set_icon(logo)
	'''
	#Screen Init
	pygame.display.set_caption("2dPyGame")
	screen = pygame.display.set_mode(DISPLAY_WINDOW)

	#Background Init
	bg = Background(screen)
	bg.draw(0,0)
	update_background_x = 0
	update_background_y = 0

	#Player Init
	p = Player(screen)
	p_facing = 'up'
	p.draw(p_facing)

	# Loop Init
	running = True

	# Main Loop
	begin = time.time()
	clock = pygame.time.Clock()
	while running:
		# All keys pressed, is a dictonary of bools of all keys
		key=pygame.key.get_pressed()
		# Key Updates
		if key[pygame.K_UP] == 1:
			update_background_y = -1
			p_facing = 'up'
		elif key[pygame.K_DOWN] == 1:
			update_background_y = 1
			p_facing = 'down'
		else:
			update_background_y = 0

		if key[pygame.K_RIGHT] == 1:
			update_background_x = 1
			p_facing = 'right'
		elif key[pygame.K_LEFT] == 1:
			update_background_x = -1
			p_facing = 'left'
		else:
			update_background_x = 0

		if key[pygame.K_UP] != 1 and key[pygame.K_DOWN] != 1 and key[pygame.K_RIGHT] != 1 and key[pygame.K_LEFT] != 1 :
			p_facing = None
		
		# All Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		#Debug prints
		#print(key[pygame.K_w],key[pygame.K_s],key[pygame.K_a],key[pygame.K_d],update_background_x,update_background_y)
		#print(bg.curr_X,bg.curr_Y,bg.surface_w,bg.surface_h)

		# All Draws
		bg.draw(update_background_x,update_background_y)
		p.draw(p_facing)

		# For all the Draw operations 1 flip for frame
		pygame.display.flip()

		# Timing game loop
		clock.tick(30)
		now = time.time()
		#print("Loop : {0} seconds ".format(now - begin))
		begin = now

if __name__=="__main__":

	main()