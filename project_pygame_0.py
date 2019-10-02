import pygame


pygame.init()
size = 300, 300
screen = pygame.display.set_mode(size)

pygame.draw.rect(screen, pygame.Color('red'), (0, 0, 100, 100), 0)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()