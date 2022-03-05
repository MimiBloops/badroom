import pygame
from element import *

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Player(element):

    def __init__(self,pos_x,pos_y,textureName=None):
        super().__init__(pos_x,pos_y,textureName)
        self.health = 3
        self.max_health = 3
        self.attack = 10
        self.velocity = 5
        self.screenHight = pygame.display.get_surface().get_height()
        self.screenWidth = pygame.display.get_surface().get_width()
        
    def event(self):
        super().event(self)

    def update(self):
        super().update()
        self.texture_rect.y = self.screenHight/1.35
        self.texture_rect.x = self.screenWidth/8

    def render(self,screen):
        super().render(screen)