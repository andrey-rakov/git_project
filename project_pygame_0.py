import pygame


pygame.init()
pygame.display.set_caption('Рисуем флаг')
size = 300, 300
screen = pygame.display.set_mode(size)

pygame.draw.rect(screen, pygame.Color('brown'), (0, 0, 10, 300), 0)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()