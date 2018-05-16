import pygame


class MiAgDa():

    def __init__(self):

        print("Start Mi Ag Da")

        pygame.init()
        display_surface = pygame.display.set_mode((800, 480), pygame.NOFRAME)
        print(pygame.display.Info())