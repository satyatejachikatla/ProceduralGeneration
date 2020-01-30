import pygame
import resources as rs

import itertools
import time
import numpy as np

DISPLAY_WINDOW_X , DISPLAY_WINDOW_Y = (500,500)
DISPLAY_WINDOW = (DISPLAY_WINDOW_X,DISPLAY_WINDOW_Y)

BLACK = (0,0,0)

class Background:
	def __init__(self,screen):
		self.screen = screen
		self.img    = rs.ground

		#Calucalte minimum buffer surface size
		def gcd(a,b): 
			if a == 0: 
				return b 
			return gcd(b % a, a)
		def lcm(a,b): 
			return (a*b) / gcd(a,b) 
  
		self.surface_w = int(lcm(screen.get_width()*2,self.img.get_width()))
		self.surface_h = int(lcm(screen.get_height()*2,self.img.get_height()))

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

	def draw_background(self,a=0,b=0):

		#Update of the surface co-ords
		self.curr_X = (self.curr_X + a) % (self.surface_w // 2)
		self.curr_Y = (self.curr_Y + b) % (self.surface_h // 2)

		# Basic fill
		self.screen.fill(BLACK)
		
		# Cropped image from surface
		self.screen.blit(self.surface,(0,0),(self.curr_X,self.curr_Y,self.screen.get_width(),self.screen.get_height()))
		

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
	bg.draw_background(0,0)
	update_background_x = 0
	update_background_y = 0

	# Loop Init
	running = True

	# Main Loop
	begin = time.time()
	clock = pygame.time.Clock()
	while running:
		# All keys pressed, is a dictonary of bools of all keys
		key=pygame.key.get_pressed()
		
		# All Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if key[pygame.K_w] == 1:
				update_background_y = -1
			if key[pygame.K_s] == 1:
				update_background_y = 1
			if key[pygame.K_d] == 1:
				update_background_x = 1
			if key[pygame.K_a] == 1:
				update_background_x = -1

		print(key[pygame.K_w],key[pygame.K_s],key[pygame.K_a],key[pygame.K_d],update_background_x,update_background_y)

		# All Draws
		bg.draw_background(update_background_x,update_background_y)

		# For all the Draw operations 1 flip for frame
		pygame.display.flip()

		# Timing game loop
		clock.tick(30)
		now = time.time()
		#print("Loop : {0} seconds ".format(now - begin))
		begin = now

if __name__=="__main__":

	main()