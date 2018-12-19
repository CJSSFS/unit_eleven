import pygame, sys
from pygame.locals import *
import block
import random

pygame.init()
X_SPEED = 3
Y_SPEED = 3
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
main_window = pygame.display.set_mode((500, 500), 32, 0)
pygame.display.set_caption("Animation")

BLUE = (0, 0, 255)
WIDTH = 25
HEIGHT = 25
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
group = pygame.sprite.Group()
for x in range(10):
    my_block = block.Block(main_window, WIDTH, HEIGHT, BLUE)
    group.add(my_block)
    my_block.rect.x = random.randint(WIDTH, WINDOW_WIDTH-WIDTH)
    my_block.rect.y = random.randint(WIDTH, WINDOW_WIDTH-WIDTH)


while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

    main_window.fill(WHITE)
    for a_brick in group:
        a_brick.move()
        group.remove(a_brick)
        a_brick.collide(group)
        group.add(a_brick)
        main_window.blit(a_brick.image, a_brick.rect)

    pygame.display.update()





