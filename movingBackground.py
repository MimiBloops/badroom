from element import *

class movingBackground(element):
    def __init__(self,pos_x,pos_y,textureName=None):
        super().__init__(pos_x,pos_y)
        if textureName is not None:
            self.texture = pygame.image.load(resource_path("ressources/" + textureName)).convert()
            self.texture_rect = self.texture.get_rect()
            self.texture_rect.x = pos_x
            self.texture_rect.y = pos_y

    def update(self):
        super().update()
        self.texture_rect.x -= 5