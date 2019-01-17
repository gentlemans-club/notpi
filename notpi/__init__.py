import pygame
import sys
import numpy as np

class NotPi:
    def __init__(self, scale=16):
        self.pixels = [[0, 0, 0]] * 64
        self.scale = scale
        pygame.init()
        self.size = width, height = 8*self.scale, 8*self.scale
        self.screen = pygame.display.set_mode(self.size)
        self.update()

    def set_pixels(self, pixels):
        self.pixels = pixels
        self.update()

    def get_pixels(self):
        return self.pixels

    def flip_v(self, redraw=True):
        """
        Flips the image on the canvas vertically.
        """
        self.pixels = np.flipud(self.pixels)
        if redraw:
            self.update()


    def update(self):
        rects = []
        for idx, pixel in enumerate(self.pixels):
            x = idx % 8
            y = idx // 8

            rects.append((pygame.Rect(x*self.scale, y*self.scale, self.scale, self.scale), pixel))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        self.screen.fill((0,0,0))
        for rect, color in rects:
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()
