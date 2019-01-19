import sys
import pygame

class Stick:
    def __init__(self, event):
        self.event = event

    def get_events(self):
        eventlist = []
        for event in self.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                action = "pressed"
            elif event.type == pygame.KEYUP:
                action = "released"
            else:
                continue
            if event.key == pygame.K_LEFT:
                key = "left"
            elif event.key == pygame.K_RIGHT:
                key = "right"
            elif event.key == pygame.K_UP:
                key = "up"
            elif event.key == pygame.K_DOWN:
                key = "down"
            elif event.key == pygame.K_RETURN:
                key = "enter"
            else:
                continue
            eventlist.append(Event(action, key))
        return eventlist

class Event:
    def __init__(self, action, direction):
        self.action = action
        self.direction = direction
