def allPossibleMoves(x, onBoard, whiteToMove, castles, enPassant):
    validMoveList = []
    #Pawn promotions, moving in/out of check, castling.
    #all of the above still need to be completed.

    if whiteToMove:
        colour = "white"
        oppositeColour = "abcdef"
        sameColour = "ghijkl"
    else:
        colour = "black"
        oppositeColour = "ghijkl"
        sameColour = "abcdef"

    pieceType = onBoard[x-1]

    pieces = sameColour+oppositeColour

    if pieceType == "e" or pieceType == "k":#all possible moves if piece on x is king.
        listKingMoves = [x-9, x-8, x-7, x-1, x+1, x+7, x+8, x+9]
        if 9 > x:
            listKingMoves = [e for e in listKingMoves if e not in (x-9, x-8, x-7)]
        if x > 56:
            listKingMoves = [e for e in listKingMoves if e not in (x+7, x+8, x+9)]
        if x%8 == 0:
            listKingMoves = [e for e in listKingMoves if e not in (x-7, x+1, x+9)]
        if (x-1)%8 == 0:
            listKingMoves = [e for e in listKingMoves if e not in (x-9, x-1, x+7)]

        for i in range(len(listKingMoves)):
            if onBoard[listKingMoves[i]-1] not in sameColour:
                validMoveList.append(listKingMoves[i])

        #need to cover castling, active check, and moving into check.
        return validMoveList

    if pieceType == "b" or pieceType == "h":#all possible moves if piece on x is knight.
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
            if onBoard[listKnightMoves[i]-1] not in sameColour:
                validMoveList.append(listKnightMoves[i])
        return validMoveList

    if pieceType == "j" or pieceType == "d" or pieceType == "c" or pieceType == "i" or pieceType == "a" or pieceType == "g":#all possible moves if piece on x is queen, rook or bishop.
        listQueenMoves = []
        listBishopMoves = []
        listRookMoves = []

        canMoveRight = True
        canMoveLeft = True
        canMoveUp = True
        canMoveDown = True

        upRight = True
        upLeft = True
        downRight = True
        downLeft = True

        for j in range(7):
            if canMoveRight == True:
                if (x +j)%8 != 0:
                    if onBoard[x+j] not in sameColour:
                        listRookMoves.append(x +j+1)
                    else: canMoveRight = False
                    if onBoard[x+j] in oppositeColour:
                        listRookMoves.append(x + j + 1)
                        canMoveRight = False
                else: canMoveRight = False

            if canMoveLeft == True:
                if (x -(j+1))%8 != 0:
                    if onBoard[x - (j+1)-1] not in sameColour:
                        listRookMoves.append(x-(j+1))
                    else: canMoveLeft = False
                    if onBoard[x - (j+1)-1] in oppositeColour:
                        listRookMoves.append(x - (j + 1))
                        canMoveLeft = False
                else: canMoveLeft = False

            if canMoveUp == True:
                if (x-(j+1)*8) > 0:
                    if onBoard[x-(j+1)*8-1] not in sameColour:
                        listRookMoves.append(x-(j+1)*8)
                    else: canMoveUp = False
                    if onBoard[x-(j+1)*8-1] in oppositeColour:
                        listRookMoves.append(x - (j + 1) * 8)
                        canMoveUp = False
                else: canMoveUp = False

            if canMoveDown == True:
                if (x+(j+1)*8) < 65:
                    if onBoard[x+(j+1)*8-1] not in sameColour:
                        listRookMoves.append(x+(j+1)*8)
                    else: canMoveDown = False
                    if onBoard[x+(j+1)*8-1] in oppositeColour:
                        listRookMoves.append(x + (j + 1) * 8)
                        canMoveDown = False
                else: canMoveDown = False

            #bishopMoves
            if upRight == True:
                if (x - (j+1)*7-1)%8 != 0 and (x - (j+1)*7) > 0:
                    if onBoard[x - (j+1)*7-1] not in sameColour:
                        listBishopMoves.append(x - (j+1)*7)
                    else: upRight = False
                    if onBoard[x - (j + 1) * 7 - 1] in oppositeColour:
                        listBishopMoves.append(x - (j + 1) * 7)
                        upRight = False
                else: upRight = False

            if upLeft == True:
                if (x - (j+1)*9)%8 != 0 and (x - (j+1)*9) > 0:
                    if onBoard[x - (j+1)*9-1] not in sameColour:
                        listBishopMoves.append(x - (j+1)*9)
                    else: upLeft = False
                    if onBoard[x - (j + 1) * 9 - 1] in oppositeColour:
                        listBishopMoves.append(x - (j + 1) * 9)
                        upLeft = False
                else: upLeft = False

            if downLeft == True:
                if (x + (j+1)*7)%8 != 0 and (x + (j+1)*7) < 65:
                    if onBoard[x + (j+1)*7-1] not in sameColour:
                        listBishopMoves.append(x + (j+1)*7)
                    else: downLeft = False
                    if onBoard[x + (j+1)*7-1] in oppositeColour:
                        listBishopMoves.append(x + (j+1)*7)
                        downLeft = False
                else: downLeft = False

            if downRight == True:
                if (x + (j+1)*9-1)%8 != 0 and (x + (j+1)*9) < 65:
                    if onBoard[x + (j+1)*9-1] not in sameColour:
                        listBishopMoves.append(x + (j+1)*9)
                    else: downRight = False
                    if onBoard[x + (j + 1) * 9 - 1] in oppositeColour:
                        listBishopMoves.append(x + (j + 1) * 9)
                        downRight = False
                else: downRight = False


        if pieceType == "a" or pieceType == "g":
            return listRookMoves
        if pieceType == "c" or pieceType == "i":
            return listBishopMoves
        if pieceType == "j" or pieceType == "d":
            return listBishopMoves + listRookMoves

    if pieceType == "f" or pieceType == "l":#all moves for black pawns
        listBlackPawnMoves = []
        listWhitePawnMoves = []

        if colour == "black":
            if onBoard[x+7] not in pieces:
                listBlackPawnMoves.append(x+8)
                if x < 17:
                    if onBoard[x+15] not in pieces:
                        listBlackPawnMoves.append(x+16)
            if onBoard[x+6] in oppositeColour:
                listBlackPawnMoves.append(x+7)
            if onBoard[x+8] in oppositeColour:
                listBlackPawnMoves.append(x + 9)
            return listBlackPawnMoves
        else:
            if onBoard[x-9] not in pieces:
                listWhitePawnMoves.append(x-8)
                if x > 48:
                    if onBoard[x-17] not in pieces:
                        listWhitePawnMoves.append(x-16)
            if onBoard[x-7] in oppositeColour:
                listWhitePawnMoves.append(x-7)
            if onBoard[x-10] in oppositeColour:
                listWhitePawnMoves.append(x - 9)
            return listWhitePawnMoves


        #Check FEN notation for square names, if square name exists, add the x value of the square to a pieces clone, and check the clone for pawn capture squares.

    #need to include promotion

#onBoard = 'abcdecbaff0fffff0000000000f000000000l00000000h00llll0lllghijki0g'

#example = allPossibleMoves(x, onBoard, True, True, True)
#print(example)