import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        # finish setting the class variables to the parameters
        self.main_surface = main_surface

        # Create a surface with the correct height and width
        self.image = pygame.image.load("stick.png")
        # self.image.fill(self.color)

        # Get the rect coordinates
        self.rect = self.image.get_rect()
        pygame.display.update()

        # Fill the surface with the correct color

    def move(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

