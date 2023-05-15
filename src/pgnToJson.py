import re
# Convert 5. Bxc8 {[%clk 0:09:28]} 5... Qxc8 {[%clk 0:09:34.2]} --> [..., [ [B, c8, x], [Q, c8, x] ], ...]
# Format : [[2 elements]], [Piece, position, action]
# Eg Nf6 --> [N, f6, null] , e5--> [null, e5, null]


#read single file function
def convertPGN (PGNPath, JSONPath) :
    file_path = PGNPath
    with open(file_path, "r") as file:
        for line in file:
            #process only game lines
            if line[0] == "1":
                numMoves = getMoves(line)
                gameArray = filterGame (line, numMoves)
                finalGame = filterMoves (gameArray)
                print(finalGame)
                writeToJson(finalGame, JSONPath)

#return length (number of moves) of game
def getMoves(game) :
    pattern = r'\d+'
    matches = re.findall(pattern, game)
    moves = 0
    for match in matches:
        if int(match) == moves + 1:
            moves += 1
    return moves


def filterGame (game, numMoves) :
    rows = numMoves
    gameArray = []
    i = 2
    for i in range(2, numMoves+1):
        splitGame = game.split(' ' + str(i) + '. ')
        move = splitGame[0]
        game = str(i) +'. ' + splitGame[1]
        gameArray.append(move)
        i += 1
    gameArray.append(game)
    return gameArray

def filterMoves (gameArray):
    finalGame = []
    i = 1
    for move in gameArray:
        moves = move.split(' ')
        moveWhite = treatMove(moves[1])
        moveBlack = treatMove(moves[5])
        finalGame.append([moveWhite, moveBlack])
    return finalGame

def treatMove(move):
    special_chars = ['+', 'x', '#', '=']
    piece = None
    action = []
    if move[0].isupper():
        if move[0] == 'O':
            if move == 'O-O-O':
                action.append('long_castle')
            else:
                action.append('castle')
        else:
            piece = move[0]
            move = move[1:]
    position = move
    #special characters
    if any(char in move for char in special_chars):
        if '+' in move:
            action.append('check')
        if 'x' in move:
            action.append('capture')
            if move[0] != 'x':
                piece = move[0]
                move = move[1:]
        if '=' in move:
            position = move.find('=')
            promotePiece = move[position+1]
            move = move[:position+1] + move[position+2:]
            action.append('promote: ' + promotePiece)
        if '#' in move:
            action.append('checkmate')
        for char in special_chars:
            move = move.replace(char, '')
        position = move
    return [piece, position, action]

def writeToJson(finalGame, path) :
    print()



convertPGN("../src/PGN_DAT/unitTesting.pgn", "../src/JSON_DAT/2015-02.json")