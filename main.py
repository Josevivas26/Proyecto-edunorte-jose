import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((900, 520))
clock_fps = pygame.time.clock()
runing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            screen.fill("purple")

            pygame.display.flip()

            clock_fps.tick(60) #limites fps to 60

pygame.quit()
sys.exit()            