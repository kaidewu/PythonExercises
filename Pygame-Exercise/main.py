import pygame
import math

WIDTH, HEIGTH = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Planet')

class Planet:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.x_vel = 0
        self.y_vel - 0

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.init()

if __name__ == '__main__':
    main()