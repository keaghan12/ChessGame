#importing necessary libraries.
import numpy as np
import pygame.display


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


#defining a class for types of pieces.
class Piece():
    def __init__(self, colour, type, image):
        self.colour = colour
        self.type = type
        self.image = image

#introducing variables for each piece.
a = Piece('black', 'pawn', "blackPawn.png")
b = Piece('black', 'rook', "blackRook.png")
c = Piece('black', 'queen', "blackQueen.png")
d = Piece('black', 'king', "blackKing.png")
e = Piece('black', 'knight', "blackKnight.png")
f = Piece('black', 'bishop', "blackBishop.png")

g = Piece('white', 'pawn', "whitePawn.png")
h = Piece('white', 'rook', "whiteRook.png")
i = Piece('white', 'knight', "whiteKnight.png")
j = Piece('white', 'bishop', "whiteBishop.png")
k = Piece('white', 'queen', "whiteQueen.png")
l = Piece('white', 'king', "whiteKing.png")

#pygame initialization, window name and image import.
pygame.init()
screen = pygame.display.set_mode((1200, 800))
background = pygame.image.load("background.png")
pygame.display.set_caption("Keaghan's Chess Game")

#Associating a type of piece in square from string.
ID = 'abcdefghijkl'
def letterToImage(letter):
    if letter == ID[0]:
        return a.image
    elif letter == ID[1]:
        return b.image
    elif letter == ID[2]:
        return c.image
    elif letter == ID[3]:
        return d.image
    elif letter == ID[4]:
        return e.image
    elif letter == ID[5]:
        return f.image
    elif letter == ID[6]:
        return g.image
    elif letter == ID[7]:
        return h.image
    elif letter == ID[8]:
        return i.image
    elif letter == ID[9]:
        return j.image
    elif letter == ID[10]:
        return k.image
    elif letter == ID[11]:
        return l.image

#time
clock = pygame.time.Clock()

#declaring the initial position of the board in terms of associated variables.
onBoard = "befcdfebaaaaaaaa00000000000000000000000000000000gggggggghijkljih"


#Main menu screen:
    #new game
        #start
        #optiona
            #time limit
            #increment
            #1 player/2 player
                #white
                #black
                #random
    #sound
        #music on/off
        #Sound effects on/off



    #If mouse is above pixels of button
        #increase button size by 10%
            #if mouse clicks while over pixels of button
                #if mouse releases while over pixels of button
                    #button -> true

#Gameloop
running = True
while running:
    screen.blit(background, (0, 0))
    for m in range(64):
            letter = onBoard[m]
            if letter in ID:
                screen.blit(pygame.image.load(letterToImage(letter)), (coordinates[m]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #continue all game window code here.

        pygame.display.update()
    clock.tick(60)