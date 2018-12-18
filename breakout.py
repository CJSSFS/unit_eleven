import pygame, sys
from pygame.locals import *
import brick


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3
    number_bricks = 9
    HEIGHT = 20
    SPACE = 5

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLACK, WHITE]

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    for c in range(5):
        x = (WIDTH + SPACE) * c
        color = colors[c]

    pygame.init()
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    x = 0
    y = BRICK_Y_OFFSET
    my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, colors[1])
    my_brick.rect.x = x
    my_brick.rect.y = y
    main_surface.blit(my_brick.image, my_brick.rect)

    WIDTH = (500 - (number_bricks * SPACE)) / number_bricks

    for c in range(5):
        x = (WIDTH + SPACE) * c
        colors = colors[c]

    for b in range(number_bricks):
        my_brick = brick.Brick(WIDTH, HEIGHT, colors, main_surface)
        my_brick.draw_brick(x, y)
        x += WIDTH + SPACE
    number_bricks = number_bricks

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

            pygame.display.update()


main()
