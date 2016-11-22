import pygame
from pygame.locals import *
import sys

#initialie the pygame engine
pygame.init()

#first we need a screen to display all the thins, 800x800 is the resolution
screen = pygame.display.set_mode((800, 800))

#let's have a sample background image
background = pygame.image.load("niceimage.png").convert()

#blit function prints the background on to the screen
screen.blit(background,(0,0))

#This is called the Game Loop [VERY IMPORTANT]
#This is where all the game updates, input handling happends
while 1:
	#Here's how we handle keyboard input
	#This code simply check if we pressed something and end the program
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	
	#THIS LINE IS CRITICAL
	#if you dont include this line, nothing will be printed on screen
	pygame.display.update()
