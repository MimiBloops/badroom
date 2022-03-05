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
        super().__init__(pos_x,pos_y,textureName=None)
        self.health = 3
        self.max_health = 3
        self.attack = 10
        self.velocity = 5
        
    def event(self):
        super().event(self)

    def update(self):
        super().update() 

    def render(self,screen):
        super().render(screen)