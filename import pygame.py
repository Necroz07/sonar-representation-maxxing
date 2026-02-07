import pygame
import math
import time

pygame.init()

screen=pygame.display.set_mode((800,800))

clock=pygame.time.Clock()

running=True

counter = 0

while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    clock.tick(60)  # limits FPS to 60

pygame.quit()
        



        
    
    
