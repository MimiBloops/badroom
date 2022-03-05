import pygame
import element as elmt
import elementManager as elmtManager
from Player import *

import sys
import os

from movingBackground import movingBackground

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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()

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
        self.playerInitialized = False
        #self.sound_manager = SoundManager()
        pygame.display.set_icon(pygame.image.load(resource_path('ressources/icon.png')))

        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.font = pygame.font.SysFont("comicsansms", 30) # initialisaTIon des font (pour le texte)
        self.initRender()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                print("GAME CLOSED")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Jeu.Player.move()
        pass

    def update(self):
        self.clock.tick(60)
        self.backgroundManager.updateElements()
        self.entityManager.updateElements()


    def render(self):
        self.backgroundManager.renderElements(self.screen, 0)
        self.entityManager.renderElements(self.screen,0)
        pygame.display.flip()

    def initRender(self):
        self.backgroundManager = elmtManager.elementManager()
        bedroomStart = movingBackground(0,0,"bedroomStart.png")
        bedroomMiddle = movingBackground(0,0,"bedroomMiddle.png")
        bedroomEnd = movingBackground(0,0,"bedroomEnd.png")
        self.backgroundManager.addElement(bedroomStart)
        self.backgroundManager.addElement(bedroomMiddle)
        self.backgroundManager.addElement(bedroomEnd)

        self.entityManager = elmtManager.elementManager()
        player = Player(0,0,"player/idle/idle.png")
        self.playerInitialized = True
        self.entityManager.addElement(player)

