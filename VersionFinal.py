import pygame
from gpiozero import Button

pygame.init()

btn_cartoon = Button(17)
btn_arnold = Button(27)

cartoon = pygame.mixer.Sound('/home/pi/Projet/Samples/Cartoon.wav')
arnold = pygame.mixer.Sound('/home/pi/Projet/Samples/Arnold.wav')

while(1):
    btn_cartoon.when_pressed = cartoon.play
    btn_arnold.when_pressed = arnold.play
