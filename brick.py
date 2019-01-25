import pygame


class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.width = width
        self.height = height
        self.color = color
        # Create a surface with the correct height and width
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)

        def draw_brick(self, x, y):
            """
            This function draws a brick
            :param x: this gives the x dimension for the brick
            :param y: this gives the y dimension for the brick
            :return:
            """
            pygame.draw.rect(self.main_surface, self.color, (x, y, self.width, self.height), 0)
            pygame.display.update()