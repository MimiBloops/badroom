import pygame
import element as elmt
import elementManager as elmtManager

import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Jeu:
    def __init__(self,title,width,height):
        pygame.init() #initalisation de pygame
        DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.title = title
        self.width = width
        self.height = height
        self.layoutEnCours = "titleScreen"        
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        self.running = True
        self.timer = False
        self.Pause = True
        self.sakuraDelay = 0
        #self.sound_manager = SoundManager()
        pygame.display.set_icon(pygame.image.load(resource_path('ressources/icon.png')))

        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.screen = pygame.display.set_mode((width,height)) # Resize la fenêtre
        self.font = pygame.font.SysFont("comicsansms", 30) # initialisaTIon des font (pour le texte)

    def event(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def initRender(self):
        self.backgroundManager = elmtManager.elementManager()
        bedroomStart = elmt.element(0,0,"bedroomStart.png")
        bedroomMiddle = elmt.element(0,0,"bedroomMiddle.png")
        bedroomEnd = elmt.element(0,0,"bedroomEnd.png")
        self.backgroundManager.addElement(bedroomStart)
        self.backgroundManager.addElement(bedroomMiddle)
        self.backgroundManager.addElement(bedroomEnd)
        pass

