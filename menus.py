#loading required images.
mainMenuD = pygame.image.load("mainMenuDefault.png")
mainMenuH = pygame.image.load("mainMenuHighlighted.png")
musicD = pygame.image.load("musicDefault.png")
musicH = pygame.image.load("musicHighlighted.png")
SFXD = pygame.image.load("SFXDefault.png")
SFXH = pygame.image.load("SFXHighlighted.png")
musicStrengthD = pygame.image.load("musicStrengthDefault.png")
musicStrengthH= pygame.image.load("musicStrengthHighlighted.png")
aboutD = pygame.image.load("aboutDefault.png")
aboutH = pygame.image.load("aboutHighlighted.png")
newGameD = pygame.image.load("newGameDefault.png")
newGameH = pygame.image.load("newGameHighlighted.png")
soundSlider = pygame.image.load("soundSlider.png")

#this class is for button clicks. This has redundancies that must be fixed on optimization.
class Button():
    Clicked = False
    def __init__ (self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        Button.Clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and Button.Clicked == False:
                Button.Clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            Button.Clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

    def put(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def highlight(self):
        highlight = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            highlight = True
            return highlight

#creates instances of button variables.
newGameHighlighted = Button(817.5, 275, newGameH)
newGameDefault = Button(817.5, 275, newGameD)
musicDefault = Button(817.5, 365, musicD)
musicHighlighted = Button(817.5, 365, musicH)
aboutDefault = Button(817.5, 455, aboutD)
aboutHighlighted = Button(817.5, 455, aboutH)
musicStrengthDefault = Button(817.5, 275, musicStrengthD)
musicStrengthHighlighted = Button(817.5, 275, musicStrengthH)
SFXDefault = Button(817.5, 365, SFXD)
SFXHighlighted = Button(817.5, 365, SFXH)
mainMenuDefault = Button(817.5, 455, mainMenuD)
mainMenuHighlighted = Button(817.5, 455, mainMenuH)
soundSliderB = Button(850, 455, soundSlider)

#importing necessary libraries and functions from other files.
import numpy as np
import pygame.display
from moves import allPossibleMoves

mainMenu = True
musicMenu = False
newGameMenu = False
aboutMenu = False

class MenuButtons():
    Clicked = False
    def __init__(self, x, y, default, highlighted):
        self.default = pygame.image.load(default)
        self.highlighted = pygame.image.load(highlighted)
        self.rect = self.highlighted.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        MenuButtons.Clicked = False

    def draw(self):
        screen.blit(self.default, (self.rect.x, self.rect.y))
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            screen.blit(self.highlighted, (self.rect.x, self.rect.y))
            if pygame.mouse.get_pressed()[0] == 1 and MenuButtons.Clicked == False:
                MenuButtons.Clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            MenuButtons.Clicked = False
        return action

#pygame initialization, window name and image import.
pygame.init()
screen = pygame.display.set_mode((1200, 800))
background = pygame.image.load("background.png")
pygame.display.set_caption("Keaghan's Chess Game")

#creates instances of button variables.
newGame = MenuButtons(817.5, 275, "newGameDefault.png", "newGameHighlighted.png")
music = MenuButtons(817.5, 365, "musicDefault.png", "musicHighlighted.png")
about = MenuButtons(817.5, 455, "aboutDefault.png", "aboutHighlighted.png")
musicStrength = MenuButtons(817.5, 275, "musicStrengthDefault.png", "musicStrengthHighlighted.png")
SFX = MenuButtons(817.5, 365, "SFXDefault.png", "SFXHighlighted.png")
normalMenu = MenuButtons(817.5, 455, "mainMenuDefault.png", "mainMenuHighlighted.png")

x = 1
#function for menus
def menu():
    global mainMenu
    global newGameMenu
    global aboutMenu
    global musicMenu


    if mainMenu == True:
        if about.draw():
            print("yes")
            aboutMenu = True
        if music.draw():
            musicMenu = True
            mainMenu = False
        if newGame.draw():
            newGameMenu = True
            mainMenu = False

    if aboutMenu == True:
        musicStrength.draw()
        SFX.draw()
        if normalMenu.draw():
            mainMenu = True
            musicMenu = False

    if musicMenu == True:
        musicStrength.draw()
        SFX.draw()
        if normalMenu.draw():
            mainMenu = True
            musicMenu = False

    if newGameMenu == True:
        musicStrength.draw()
        SFX.draw()
        if normalMenu.draw():
            mainMenu = True
            musicMenu = False


#Gameloop containing code to be run continuously.
running = True
while running:
    screen.blit(background, (0, 0))
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update()