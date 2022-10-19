#importing libraries
import pygame.display
pygame.init()

#defining colours used.
darkGrey = (61, 61, 61)
light = (250, 217, 168)
dark = (186, 158, 115)
pink = (250, 168, 223)
black = (0, 0, 0)
white = (255, 255, 255)

red = (100, 100, 100)
blue = (0, 100, 255)

BLOCK_SIZE = 95
CIRCLE_RADIUS = 35

whiteToMove = True
castles = True
enPassant = True

white_pawn = pygame.image.load("whitePawn.png")

#creating the screen background and window.
background = pygame.display.set_mode((1200, 800))
background_rect = background.get_rect()
pygame.display.flip()
pygame.display.set_caption("Keaghan's Chess Game")


#FEN notation
from convertFEN import convertFen
#FEN = "8/5k2/3p4/1p1Pp2p/pP2Pp1P/P4P1K/8/8 b - - 99 50"
#FEN = "r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1."
FEN = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
#FEN = 'PPPPPPPP/PPPPPPPP/PPPPPPPP/PPPPPPPP/8/PPPPpPPP/8/PPPPPPPP w - - 0 1'

onBoard, whiteToMove, castles, enPassant, halfMoves, fullMoves = convertFen(FEN)

from piece import pieceType

#setting up grid size, coordinates, and rectangles.
topLeft = (20, 20)
coords = []
cCoords = []
rects = []
positions = []
squareSize = 95
for i in range(8):
    y = 20 + i * squareSize
    yc = y + 17
    for j in range(8):
        x = 20 + j * squareSize
        xc = x + 17
        coords.append((x, y))
        cCoords.append((xc, yc))
        rects.append(pygame.Rect(x, y, squareSize, squareSize))
        positions.append(pygame.Rect(xc, yc, 60, 60))

rects2 = rects.copy()


from moves import allPossibleMoves

#checks for mouse position.
def mouse():
    return pygame.mouse.get_pos()


#checks if the mouse collides with something inputted
def hover(rect, pos):
    if rect.collidepoint(pos[0], pos[1]):
        return True

class Button():

    def __init__(self, text='OK', pos=(0, 0), size=(100, 50), command=None):
        font = pygame.font.SysFont(None, 35)

        self.text = text
        self.rect = pygame.Rect((0, 0), size)

        self.image_normal = pygame.Surface(size)
        self.image_normal.fill(white)
        txt_image = font.render(self.text, True, red)
        txt_rect = txt_image.get_rect(center=self.rect.center)
        self.image_normal.blit(txt_image, txt_rect)

        self.image_hover = pygame.Surface(size)
        self.image_hover.fill(red)
        txt_image = font.render(self.text, True, white)
        txt_rect = txt_image.get_rect(center=self.rect.center)
        self.image_hover.blit(txt_image, txt_rect)

        self.rect.topleft = pos

        self.hover = False

        if command:
            self.command = command

    def draw(self, screen):
        if self.hover:
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image_normal, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)

        if self.hover and self.command:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.command()

    def command(self):
        print("Click")

def print_hello():
    print("Click HELLO")


def print_world():
    print("Click WORLD")

button1 = Button(text="HELLO", pos = (900, 100))  # create button
button1.command = print_hello  # assign function to button

button2 = Button(text="WORLD", pos=(900, 300), command=print_world)  # create button and assign function

#determines colours, draws the background colours of the board.
defaultColour = []
for i in range(8):
    for j in range(8):
        if i%2 == 0:
            if j%2 == 0:
                defaultColour.append(light)
            else:
                defaultColour.append(dark)
        else:
            if j%2 == 0:
                defaultColour.append(dark)
            else:
                defaultColour.append(light)
def drawBoard():
    colour = defaultColour.copy()
    for i in range(64):
        if hover(rects[i], mouse()):
            colour[i] = pink

        pygame.draw.rect(background, colour[i], rects[i])

def updateOnBoard(moved_from, moved_to):
    print(onBoard[moved_to])
    print(onBoard[moved_from])
    #onBoard[moved_to] = onBoard[moved_from]
    onBoard[moved_from] = '0'

clock = pygame.time.Clock()
selected = None
#Main game loop
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                for i, c in enumerate(positions):
                    dx = c.centerx - event.pos[0]  # A
                    dy = c.centery - event.pos[1]  # B
                    distance_square = dx ** 2 + dy ** 2  # C^2

                    if distance_square <= CIRCLE_RADIUS ** 2:  # C^2 <= RADIUS^2
                        if onBoard[i] != '0':
                            selected = i
                            selected_offset_x = c.x - event.pos[0]
                            selected_offset_y = c.y - event.pos[1]


        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                #During release point of the piece drag, selected piece will move to closest square.

                for i in range(len(positions)):
                    if selected != None:
                        if hover(rects2[i], positions[selected]):
                            if onBoard[i] in "ghijkl":
                                whiteToMove = True
                            elif onBoard[i] in 'abcdef':
                                whiteToMove = False
                            #print(allPossibleMoves(selected+1, onBoard, whiteToMove, castles, enPassant))
                            if i+1 in allPossibleMoves(selected + 1, onBoard, whiteToMove, castles, enPassant):

                                onBoard = list(onBoard)
                                onBoard[i] = onBoard[selected]
                                onBoard[selected] = '0'
                                onBoard = ''.join(onBoard)
                                print(onBoard)

                                positions[selected].x = rects2[i].x + 17
                                positions[selected].y = rects2[i].y + 17

                            else:
                                positions[selected].x = rects2[selected].x + 17
                                positions[selected].y = rects2[selected].y + 17
                selected = None

        elif event.type == pygame.MOUSEMOTION:
            if selected is not None:
                positions[selected].x = event.pos[0] + selected_offset_x
                positions[selected].y = event.pos[1] + selected_offset_y

        button1.handle_event(event)
        button2.handle_event(event)

        background.fill(darkGrey)
        drawBoard()


        if event.type == pygame.QUIT:
            running = False
        counter = 0
        for c in positions:
            #Hitbox circles for pieces.
            #pygame.draw.circle(background, red, c.center, CIRCLE_RADIUS)

            variable = pieceType(onBoard[counter])
            if variable != None:
                background.blit(variable, (c.centerx - 39, c.centery - 40))
            counter +=1


        button1.draw(background)
        button2.draw(background)

        clock.tick(25)
        pygame.display.update()