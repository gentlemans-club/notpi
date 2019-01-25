import pygame
import sys
import os
import numpy as np
from PIL import Image
from notpi.stick import Stick

class NotPi:
    def __init__(self, scale=16):
        self.pixels = [[0, 0, 0]] * 64
        self.scale = scale
        pygame.init()
        self.size = width, height = 8*self.scale, 8*self.scale
        self.screen = pygame.display.set_mode(self.size)
        self.stick = Stick(pygame.event)
        self.low_light = False
        self.update()

    def __index_to_xy(self, index):
        return (index % 8, index // 8)

    def clear(self, *args):
        """
        Clears the LED matrix with a single colour, default is black / off
        e.g. ap.clear()
        or
        ap.clear(r, g, b)
        or
        colour = (r, g, b)
        ap.clear(colour)
        """

        black = (0, 0, 0)  # default

        if len(args) == 0:
            colour = black
        elif len(args) == 1:
            colour = args[0]
        elif len(args) == 3:
            colour = args
        else:
            raise ValueError('Pixel arguments must be given as (r, g, b) or r, g, b')

        self.set_pixels([colour] * 64)

    def show_message(
        self,
        text_string,
        scroll_speed=.1,
        text_colour=[255, 255, 255],
        back_colour=[0, 0, 0]
        ):
        print(text_string)

    def show_letter(
        self,
        s,
        text_colour=[255, 255, 255],
        back_colour=[0, 0, 0]
        ):

        """
        Displays a single text character on the LED matrix using the specified
        colours
        """

        if len(s) > 1:
            raise ValueError('Only one character may be passed into this method')

        print(s)

    def set_pixels(self, pixels):
        self.pixels = pixels
        self.update()

    def get_pixels(self):
        return self.pixels

    def set_rotation(self, r=0, redraw=True):
        self.update()

    def set_pixel(self, x, y, *args):
        pixel_error = 'Pixel arguments must be given as (r, g, b) or r, g, b'

        if len(args) == 1:
            pixel = args[0]
            if len(pixel) != 3:
                raise ValueError(pixel_error)
        elif len(args) == 3:
            pixel = args
        else:
            raise ValueError(pixel_error)

        if x > 7 or x < 0:
            raise ValueError('X position must be between 0 and 7')

        if y > 7 or y < 0:
            raise ValueError('Y position must be between 0 and 7')

        for element in pixel:
            if element > 255 or element < 0:
                raise ValueError('Pixel elements must be between 0 and 255')

        self.pixels[x + y*8] = list(pixel)
        self.update()

    def get_pixel(self, x, y):
        """
        Returns a list of [R,G,B] representing the pixel specified by x and y
        on the LED matrix. Top left = 0,0 Bottom right = 7,7
        """

        if x > 7 or x < 0:
            raise ValueError('X position must be between 0 and 7')

        if y > 7 or y < 0:
            raise ValueError('Y position must be between 0 and 7')

        return self.pixels[x + y*8]

    def show_image(self, file_path, redraw=True):
        """
        Accepts a path to an 8 x 8 image file and updates the LED matrix with
        the image
        """

        if not os.path.exists(file_path):
            raise IOError('%s not found' % file_path)

        img = Image.open(file_path).convert('RGB')
        pixel_list = list(map(list, img.getdata()))

        if redraw:
            self.set_pixels(pixel_list)

        return pixel_list

    def flip_v(self, redraw=True):
        """
        Flips the image on the canvas vertically.
        """
        self.pixels = np.flipud(self.pixels)
        if redraw:
            self.update()

    def flip_h(self, redraw=True):
        """
        Flips the image on the canvas horizontally.
        """
        self.pixels = np.fliplr(self.pixels)
        if redraw:
            self.update()


    def update(self):
        rects = []
        for idx, pixel in enumerate(self.pixels):
            x, y = self.__index_to_xy(idx)

            rects.append((pygame.Rect(x*self.scale, y*self.scale, self.scale, self.scale), pixel))

        self.screen.fill((0,0,0))
        for rect, color in rects:
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()
