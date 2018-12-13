import pygame, sys
from pygame.locals import *
import block

pygame.init()
X_SPEED = 3
Y_SPEED = 3
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
main_window = pygame.display.set_mode((500, 500), 32, 0)
pygame.display.set_caption("Animation")

BLUE = (0, 0, 255)
WIDTH = 25
HEIGHT = 25
WHITE = (255, 255, 255)


my_block = block.Block(main_window, WIDTH, HEIGHT, BLUE)
my_block.rect.x = 10
my_block.rect.y = 10
main_window.blit(my_block.image, my_block.rect)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

    main_window.fill(WHITE)
    my_block.rect.left += X_SPEED
    my_block.rect.top += Y_SPEED
    if my_block.rect.left <= 0 or my_block.rect.right >= WINDOW_WIDTH:
        X_SPEED = -Y_SPEED
    main_window.blit(my_block.image, my_block.rect)
    pygame.display.update()





