#importing necessary libraries and functions from other files.
import numpy as np
import pygame.display
from moves import allPossibleMoves

#declaring the initial position of the board in terms of associated variables.
onBoard = "befcdfebaaaaaaaa00000000000000000000000000000000gggggggghijkljih"
#onBoard = "0000a0000b0000d00000e000f0000c000g0000h0i000j000k000l00000000000"
#onBoard = "00a0a00000a0a00000a0a000000c000000a0a000000000000000000000000000"
#onBoard = "0000000000k00000000k0000k0000k00000k0000000k0000000000k000k000000"
#onBoard = "0000000000000000000000000000000000a000000ggg0000000000000000000000"

#create a grid of squares as per usual chess notation. not currently being used
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
for i in range(8):
    topLeftY = 21 + i*95
    for j in range(8):
        topLeftX = 23 + j*95
        rectangle.append(pygame.Rect(topLeftX, topLeftY, 95, 95))
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
        colourMoves = (255, 154, 153)
        colourSquare = (255, 255, 255)
        pos = pygame.mouse.get_pos()
        for i in range(64):
            if hover(rectangle[i], pos):
                if self.letter == onBoard[i]:
                    something = i
                    squares = allPossibleMoves(something+1, self.colour, self.type, onBoard)
                    for j in range(len(squares)):
                        pygame.draw.rect(screen, colourMoves, rectangle[squares[j] - 1])
                        pygame.draw.rect(screen, colourSquare, rectangle[i])


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
    highlightMoves()
    fillScreenBoard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update()