import pygame
import math
import time



pygame.init()

font = pygame.font.SysFont(None, 169)

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("goooooon")

wave_surf = pygame.Surface((600, 600), pygame.SRCALPHA)

bg = pygame.image.load("background.png").convert()
bg = pygame.transform.scale(bg, (600,600))

obj = pygame.image.load("object.png").convert_alpha()
obj = pygame.transform.scale(obj, (50, 50))




clock=pygame.time.Clock()

running=True

wave_radius = 0

wave_speed = 3


last_time = pygame.time.get_ticks()




inc=True

while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    wave_surf = pygame.Surface((600,600), pygame.SRCALPHA)

    pygame.draw.circle(wave_surf, (0, 0, 0, 120), (300, 300), wave_radius, 3)

    screen.blit(bg, (0,0))
    screen.blit(obj, (275,275))
    screen.blit(wave_surf, (0, 0))

    if inc==True:
        wave_radius += wave_speed

    elif inc==False:
        wave_radius -= wave_speed




    if wave_radius > 375:
        inc = False

    if wave_radius < 0:
        inc = True
    
    pygame.display.flip()

    
    clock.tick(60)  # limits FPS to 60


pygame.quit()



        
    
    
