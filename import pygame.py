import pygame
import math
import time



pygame.init()

font = pygame.font.SysFont(None, 169)

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("goooooon")

bg = pygame.image.load("background.png").convert()
bg = pygame.transform.scale(bg, (600,600))

obj = pygame.image.load("object.png").convert_alpha()
obj = pygame.transform.scale(obj, (50, 50))


wave_surf = pygame.Surface((600, 600), pygame.SRCALPHA)


clock=pygame.time.Clock()

running=True

counter = 0

wave_radius = 0

wave_speed = 4


last_time = pygame.time.get_ticks()






while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            

    current_time = pygame.time.get_ticks()

    

    if current_time - last_time >=1000:
        
        counter+=1
        last_time = current_time

        if counter > 10:
            running = False


    wave_surf = pygame.Surface((600,600), pygame.SRCALPHA)

    pygame.draw.circle(wave_surf, (0, 255, 255, 120), (275, 275), wave_radius, 3)

            

    screen.blit(bg, (0,0))
    screen.blit(obj, (275,275))

    wave_radius += wave_speed


    if wave_radius > 900:
        wave_radius = 0
    

    text = font.render(str(counter), True, "black")

    text_rect = text.get_rect(center=(300,300))

    
        
    screen.blit(text, text_rect)

    pygame.display.flip()

    

    clock.tick(60)  # limits FPS to 60

pygame.quit()



        
    
    
