import pygame
import os

DISPLAY_WINDOW_X , DISPLAY_WINDOW_Y = (500,500)
DISPLAY_WINDOW = (DISPLAY_WINDOW_X,DISPLAY_WINDOW_Y)

DIR = os.path.dirname(os.path.realpath(__file__))

#Current ground image is not veritally seemless
_ground = DIR+'/ground.jpg'
ground = pygame.image.load(_ground)

_grass = DIR+'/grass.jpg'
grass = pygame.image.load(_grass)
grass = pygame.transform.scale(grass,(DISPLAY_WINDOW_X,DISPLAY_WINDOW_Y))

_player_sprite = DIR+'/player_sprite.png'
player_sprite  = pygame.image.load(_player_sprite)
#player_sprite = pygame.transform.scale(player_sprite,(DISPLAY_WINDOW_X,DISPLAY_WINDOW_Y))
player_sprite_w = player_sprite.get_width()
player_sprite_w_animations = 12
player_sprite_h = player_sprite.get_height()
player_sprite_h_animations = 4
player = {
	'animation' : {
					'up'    : [ pygame.Surface((player_sprite_w//player_sprite_w_animations,player_sprite_h//player_sprite_h_animations)) for _ in range(player_sprite_w_animations)  ] ,
					'down'  : [ pygame.Surface((player_sprite_w//player_sprite_w_animations,player_sprite_h//player_sprite_h_animations)) for _ in range(player_sprite_w_animations)  ] ,
					'left'  : [ pygame.Surface((player_sprite_w//player_sprite_w_animations,player_sprite_h//player_sprite_h_animations)) for _ in range(player_sprite_w_animations)  ] ,
					'right' : [ pygame.Surface((player_sprite_w//player_sprite_w_animations,player_sprite_h//player_sprite_h_animations)) for _ in range(player_sprite_w_animations)  ]  
				}
}
for key in player['animation']:
	if key == 'up':
		j = 3
	elif key == 'down':
		j = 0
	elif key == 'left':
		j = 1
	elif key == 'right':
		j = 2
	else:
		raise Exception('Failed to load player sprite')
	for i in range(len(player['animation'][key])):
		player['animation'][key][i].blit(player_sprite,(0,0),(i*(player_sprite_w//player_sprite_w_animations),
															 j*(player_sprite_h//player_sprite_h_animations),
															 player['animation'][key][i].get_width(),
															 player['animation'][key][i].get_height()))
		player['animation'][key][i].set_colorkey((0,0,0))
'''
Generate resources
'''
# Generate default Ground Sprite
##import cv2