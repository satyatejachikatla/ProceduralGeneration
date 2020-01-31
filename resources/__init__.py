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

'''
Generate resources
'''
# Generate default Ground Sprite
##import cv2