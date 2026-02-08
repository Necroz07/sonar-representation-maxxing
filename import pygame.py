import pygame
import math
import time



pygame.init()

font = pygame.font.SysFont(None, 169)

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Timer Test!!!! goooooon")

clock=pygame.time.Clock()

running=True

counter = 0

last_time = pygame.time.get_ticks()


while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()

    if current_time - last_time >=1000:


        print(counter)
        counter+=1
        last_time = current_time

        if counter > 10:
            running = False

    screen.fill("purple")

    text = font.render(str(counter), True, "black")

    text_rect = text.get_rect(center=(400,400))

    
        
    screen.blit(text, text_rect)

    pygame.display.flip()

    

    clock.tick(60)  # limits FPS to 60

pygame.quit()
        



        
    
    
