import pygame
black_bishop = pygame.image.load("blackBishop.png")
black_knight = pygame.image.load("blackKnight.png")
black_queen = pygame.image.load("blackQueen.png")
black_king = pygame.image.load("blackKing.png")
black_rook = pygame.image.load("blackRook.png")
black_pawn = pygame.image.load("blackPawn.png")

white_bishop = pygame.image.load("whiteBishop.png")
white_knight = pygame.image.load("whiteKnight.png")
white_queen = pygame.image.load("whiteQueen.png")
white_king = pygame.image.load("whiteKing.png")
white_rook = pygame.image.load("whiteRook.png")
white_pawn = pygame.image.load("whitePawn.png")

def pieceType(type):

    if type == 'a':
        return black_rook
    elif type == 'b':
        return black_knight
    elif type == 'c':
        return black_bishop
    elif type == 'd':
        return black_queen
    elif type == 'e':
        return black_king
    elif type == 'f':
        return black_pawn

    if type == 'g':
        return white_rook
    elif type == 'h':
        return white_knight
    elif type == 'i':
        return white_bishop
    elif type == 'j':
        return white_queen
    elif type == 'k':
        return white_king
    elif type == 'l':
        return white_pawn

    else:
        return None