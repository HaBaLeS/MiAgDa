import pygame


class BaseGadget:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def render_gadget(self):
        return pygame.Surface(self.size, pygame.SRCALPHA)


class TextFromUrlGadget(BaseGadget):

    def __init__(self, config):
        super(TextFromUrlGadget, self).__init__("hugo", (200, 200))