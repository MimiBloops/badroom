from element import *

class movingBackground(element):
    def __init__(self,pos_x,pos_y,textureName=None):
        super().__init__(pos_x,pos_y,textureName)

    def update(self):
        super().update()
        self.texture_rect.x -= 5