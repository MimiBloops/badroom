import pygame
import element as elmt

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Player(elmt):

    def __init__(self,pos_x,pos_y,textureName=None):
        player = Player(pos_x,pos_y)
        super().__init__
        self.health = 3
        self.max_health = 3
        self.attack = 10
        self.velocity = 5
        
    def event():
        super().event()

    def update():
        super().update() 

    def render():
        super().render()