
import pygame


class Window:
    def __init__(self, w, h, title):
        self.width = w
        self.height = h
        self.title = title

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def clear(self):
        self.win.fill((12,1,23))