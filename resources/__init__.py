import pygame
import os

DIR = os.path.dirname(os.path.realpath(__file__))

_ground = DIR+'/ground.jpg'
ground = pygame.image.load(_ground)

'''
Generate resources
'''
# Generate default Ground Sprite
##import cv2