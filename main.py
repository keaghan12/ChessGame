#importing necessary libraries and functions from other files.
import numpy as np
import pygame.display
from moves import allPossibleMoves

#declaring the initial position of the board in terms of associated variables.
onBoard = "befcdfebaaaaaaaa00000000000000000000000000000000gggggggghijkljih"
#onBoard = "0000a0000b0000d00000e000f0000c000g0000h0i000j000k000l00000000000"


#create a grid of squares as per usual chess notation.
rows = "ABCDEFGH"
cols = "87654321"
def grid(A, B):
    return [b+a for a in A for b in B]
listSquares = grid(cols, rows)
board = np.array(listSquares).reshape(8, 8)

#creating a grid with the coordinates of each square.
gridSize = 95
coordinates = []
for i in range(8):
    y = 30 + i*gridSize
    for j in range(8):
        x = 30 + j*gridSize
        coordinates.append((x, y))

rectangle = []
x = 0
for i in range(8):
    topLeftY = 21 + (i)*94.9
    for j in range(8):
        topLeftX = 23 + (j)*94.9
        rectangle.append(pygame.Rect(topLeftX, topLeftY, 94.9, 94.9))
    topLeftY = 0

def hover(rect, pos):
    if rect.collidepoint(pos[0], pos[1]):
        return True

#defining a class for types of pieces.
class Piece():
    def __init__(self, colour, type, image, letter):
        self.colour = colour
        self.type = type
        self.pic = image
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.letter = letter

    #function to colour the squares of all legal moves of the piece the mouse is hovering over.
    def mouseOverlap(self):
        colourRect = (255, 154, 153)
        pos = pygame.mouse.get_pos()
        for i in range(64):
            if hover(rectangle[i], pos):
                if self.letter == onBoard[i]:
                    something = i
                    squares = allPossibleMoves(something+1, self.colour, self.type)
                    for j in range(len(squares)):
                        pygame.draw.rect(screen, colourRect, rectangle[squares[j]-1])


#introducing variables for each piece.
a = Piece('black', 'pawn', "blackPawn.png", "a")
b = Piece('black', 'rook', "blackRook.png", "b")
c = Piece('black', 'queen', "blackQueen.png", "c")
d = Piece('black', 'king', "blackKing.png", "d")
e = Piece('black', 'knight', "blackKnight.png", "e")
f = Piece('black', 'bishop', "blackBishop.png", "f")

g = Piece('white', 'pawn', "whitePawn.png", "g")
h = Piece('white', 'rook', "whiteRook.png", "h")
i = Piece('white', 'knight', "whiteKnight.png", "i")
j = Piece('white', 'bishop', "whiteBishop.png", "j")
k = Piece('white', 'queen', "whiteQueen.png", "k")
l = Piece('white', 'king', "whiteKing.png", "l")

#pygame initialization, window name and image import.
pygame.init()
screen = pygame.display.set_mode((1200, 800))
background = pygame.image.load("background.png")
pygame.display.set_caption("Keaghan's Chess Game")

#Associating a type of piece in square from string.
ID = 'abcdefghijkl'
def letterToImage(letter):
    if letter == ID[0]:
        return a.pic
    elif letter == ID[1]:
        return b.pic
    elif letter == ID[2]:
        return c.pic
    elif letter == ID[3]:
        return d.pic
    elif letter == ID[4]:
        return e.pic
    elif letter == ID[5]:
        return f.pic
    elif letter == ID[6]:
        return g.pic
    elif letter == ID[7]:
        return h.pic
    elif letter == ID[8]:
        return i.pic
    elif letter == ID[9]:
        return j.pic
    elif letter == ID[10]:
        return k.pic
    elif letter == ID[11]:
        return l.pic

#loading required images.
mainMenuD = pygame.image.load("mainMenuDefault.png")
mainMenuH = pygame.image.load("mainMenuHighlighed.png")
musicD = pygame.image.load("musicDefault.png")
musicH = pygame.image.load("musicHighlighted.png")
SFXD = pygame.image.load("SFXDefault.png")
SFXH = pygame.image.load("SFXHighlighted.png")
musicStrengthD = pygame.image.load("musicStrengthDefault.png")
musicStrengthH= pygame.image.load("musicStrengthHighlighted.png")
aboutD = pygame.image.load("aboutDefault.png")
aboutH = pygame.image.load("abouthighlighted.png")
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

#fillsthe pieces into the current position on the window board.
def fillScreenBoard():
    for m in range(64):
        letter = onBoard[m]
        if letter in ID:
            screen.blit(pygame.image.load(letterToImage(letter)), (coordinates[m]))

#highlights the actual squares on the board.
def highlightMoves():
    a.mouseOverlap()
    b.mouseOverlap()
    c.mouseOverlap()
    d.mouseOverlap()
    e.mouseOverlap()
    f.mouseOverlap()
    g.mouseOverlap()
    h.mouseOverlap()
    i.mouseOverlap()
    j.mouseOverlap()
    k.mouseOverlap()
    l.mouseOverlap()

mainMenu = True
musicMenu = False
newGameMenu = False
#Gameloop containing code to be run continuously.
running = True
while running:
    screen.blit(background, (0, 0))
    if mainMenu == True: #I think these can be turned into functions that are much more efficient. # (then call mainMenu())
        musicDefault.put()
        if musicDefault.highlight():
            if musicHighlighted.draw():
                musicMenu = True
                mainMenu = False
        newGameDefault.put()
        if newGameDefault.highlight():
            if newGameHighlighted.draw():
                newGameMenu = True
                mainMenu = False
        aboutDefault.put()
        if aboutDefault.highlight():
            if aboutHighlighted.draw():
                aboutMenu = True
                mainMenu = False

    if musicMenu == True:
        musicStrengthDefault.put()
        if musicStrengthDefault.highlight():
            if musicStrengthHighlighted.draw():
                print("not built yet")
        SFXDefault.put()
        if SFXDefault.highlight():
            if SFXHighlighted.draw():
                print("not built yet")
        mainMenuDefault.put()
        if mainMenuDefault.highlight():
            if mainMenuHighlighted.draw():
                mainMenu = True
                musicMenu = False

    fillScreenBoard()
    highlightMoves()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update()