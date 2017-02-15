#This code was inspired by code for a dice game
#linked in the read me documentation
import pygame
from pygame.locals import *
from squishyGame import *
pygame.init()
#create our game window
window = pygame.display.set_mode((800,800))
#pass the game window into the game class
squishyGame(window)
