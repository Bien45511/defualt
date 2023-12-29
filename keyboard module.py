import pygame
import keyboard
pygame.init()
screen = pygame.display.set_mode([240, 160])
while True:
    for event in pygame.event.get():
        if event.key == pygame.K_RIGHT:
            print('Right')
        elif event.key == pygame.K_LEFT:
            print('Left')

           
        
        
