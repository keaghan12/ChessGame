#FEN notation
letters = "abcdefg"
numbers = "12345678"

whiteToMove = True

def convertFen(FEN):
    FEN = FEN.split()
    onBoard = ""
    enPassant = 0
    x = 0
    slash = 0
    castles = ""
    space = False
    once = True
    for i in range(len(FEN[0])):
        if FEN[0][i] == "r": onBoard = onBoard + "a"
        elif FEN[0][i] == "n": onBoard = onBoard + "b"
        elif FEN[0][i] == "b": onBoard = onBoard + "c"
        elif FEN[0][i] == "q": onBoard = onBoard + "d"
        elif FEN[0][i] == "k": onBoard = onBoard + "e"
        elif FEN[0][i] == "p": onBoard = onBoard + "f"

        elif FEN[0][i] == "R": onBoard = onBoard +"g"
        elif FEN[0][i] == "N": onBoard = onBoard +"h"
        elif FEN[0][i] == "B": onBoard = onBoard +"i"
        elif FEN[0][i] == "Q": onBoard = onBoard +"j"
        elif FEN[0][i] == "K": onBoard = onBoard +"k"
        elif FEN[0][i] == "P": onBoard = onBoard +"l"

        elif FEN[0][i] in numbers:
            num = numbers.find(FEN[0][i])
            for i in range(num+1):
                onBoard = onBoard + "0"

    if FEN[1] == "b":
        whiteToMove = True
    else:
        whiteToMove = False

    if FEN[2] != "-":
        castles = FEN[2]

    inte = 0
    if FEN[3] == "-":
        pass
    else:
        inte += letters.find(FEN[3][1])
        inte += (numbers.find(FEN[3][2]))*8
        inte +=1
        enPassant = inte

    halfMoves = eval(FEN[4])
    fullMoves = eval(FEN[5])

    return onBoard, whiteToMove, castles, enPassant, halfMoves, fullMoves


#FEN = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
#onBoard, whiteToMove, castles, enPassant, halfMoves, fullMoves = convertFen(FEN)

#print(onBoard)