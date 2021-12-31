def allPossibleMoves(x, colour, pieceType):

    #En-Passant, pawn promotions, moving in/out of check, castling, if pieces are in the way.
    #all of the above still need to be completed.

    if pieceType == "king":#all possible moves if piece on x is king.
        listKingMoves = [x-9, x-8, x-7, x-1, x+1, x+7, x+8, x+9]
        if 9 > x:
            listKingMoves = [e for e in listKingMoves if e not in (x-9, x-8, x-7)]
        if x > 56:
            listKingMoves = [e for e in listKingMoves if e not in (x+7, x+8, x+9)]
        if x%8 == 0:
            listKingMoves = [e for e in listKingMoves if e not in (x-7, x+1, x+9)]
        if (x-1)%8 == 0:
            listKingMoves = [e for e in listKingMoves if e not in (x-9, x-1, x+7)]


        #need to cover castling, active check, and moving into check.
        return listKingMoves

    if pieceType == "knight":#all possible moves if piece on x is knight.
        listKnightMoves = [-17, -15, -10, -6, 6, 10, 15, 17]
        if 9 > x:
            listKnightMoves = [e for e in listKnightMoves if e not in (-17, -15, -10, -6)]
        if x < 17:
            listKnightMoves = [e for e in listKnightMoves if e not in (-17, -15)]
        if x > 56:
            listKnightMoves = [e for e in listKnightMoves if e not in (6, 10, 15, 17)]
        if x > 48:
            listKnightMoves = [e for e in listKnightMoves if e not in (15, 17)]
        if x%8 == 0:
            listKnightMoves = [e for e in listKnightMoves if e not in (-15, -6, 10, 17)]
        if (x+1)%8 == 0:
            listKnightMoves = [e for e in listKnightMoves if e not in (-6, 10)]
        if (x-1)%8 == 0:
            listKnightMoves = [e for e in listKnightMoves if e not in (-17, -10, 6, 15)]
        if (x-2)%8 == 0:
            listKnightMoves = [e for e in listKnightMoves if e not in (-10, 6)]

        for i in range(len(listKnightMoves)):
            listKnightMoves[i] += x
        return listKnightMoves

    if pieceType == "queen" or pieceType == "bishop" or pieceType == "rook":#all possible moves if piece on x is queen, rook or bishop.
        listQueenMoves = []
        listBishopMoves = []
        listRookMoves = []

        canMoveRight = True
        canMoveLeft = True
        canMoveUp = True
        canMoveDown = True

        for j in range(7):
            if canMoveRight == True:
                if (x +j)%8 != 0:
                    listRookMoves.append(x +j+1)
                else:
                    canMoveRight = False

            if canMoveLeft == True:
                if (x -j-1)%8 != 0:
                    listRookMoves.append(x-j-1)
                else:
                    canMoveLeft = False

            if canMoveUp == True:
                if (x-(j+1)*8) > 0:
                    listRookMoves.append(x-(j+1)*8)
                else:
                    canMoveUp = False

            if canMoveDown == True:
                if (x+(j+1)*8) < 65:
                    listRookMoves.append(x+(j+1)*8)
                else:
                    canMoveDown = False

            if canMoveUp == True and canMoveRight == True:
                listBishopMoves.append(x-(j+1)*7)

            if canMoveRight == True and canMoveDown == True:
                listBishopMoves.append(x+(j+1)*9)

            if canMoveDown == True and canMoveLeft == True:
                listBishopMoves.append(x+(j+1)*7)

            if canMoveLeft == True and canMoveUp == True:
                listBishopMoves.append(x-(j+1)*9)

        if pieceType == "rook":
            return listRookMoves
        if pieceType == "bishop":
            return listBishopMoves
        if pieceType == "queen":
            return listBishopMoves + listRookMoves

    if pieceType == "pawn":#all moves for black pawns
        if colour == "black":
            listBlackPawnMoves = []
            if x < 17:
                listBlackPawnMoves.append(x+16)

            listBlackPawnMoves.append(x+8)
            return listBlackPawnMoves

    if pieceType == "pawn":#all moves for white pawns
        if colour == "white":
            listWhitePawnMoves = []
            if x > 48:
                listWhitePawnMoves.append(x - 16)

            listWhitePawnMoves.append(x - 8)
            return listWhitePawnMoves

    #need to include en-passant for both black and white pawns.
    #need to include promotion
