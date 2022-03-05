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
        self.jumpVelocity = 15
        self.IsJumping = False
        self.texture_rect.y = pygame.display.get_surface().get_height()/1.35
        
    def jump(self):
        self.IsJumping = True
        self.jumpVelocity = 15

    def event(self):
        super().event(self)

    def update(self):
        super().update()
        if self.IsJumping:
            self.texture_rect.y -= self.jumpVelocity
            self.jumpVelocity -= 1
            if self.jumpVelocity < 1:
                self.IsJumping = False
        else:
            self.IsJumping = False
        #self.texture_rect.y = pygame.display.get_surface().get_height()/1.35
        self.texture_rect.x = pygame.display.get_surface().get_width()/8

    def render(self,screen):
        super().render(screen)