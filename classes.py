import pygame
import os


class Player:
    def __init__(self, screen, clock):
        self.health = 500
        self.x = 0
        self.y = 400
        self.clock = clock

        self.width = 125
        self.hieght = 320
        
        
