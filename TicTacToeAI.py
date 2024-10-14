
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    return board[position] == ' '


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if checkDraw():
            print("It's a draw!")
            exit()

        if checkForWin():
            if letter == bot:
                print("Bot wins!")
            else:
                print("Player wins!")
            exit()
    else:
        print("Position is occupied! Please try another.")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)


def checkForWin():
    win_positions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]

    for line in win_positions:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return True
    return False


def checkWhichMarkWon(mark):
    return any(
        board[a] == board[b] == board[c] == mark
        for a, b, c in [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    )


def checkDraw():
    return all(board[key] != ' ' for key in board.keys())


def playerMove():
    position = int(input("Enter the position for 'O': "))
    insertLetter(player, position)


def compMove():
    bestScore = -float('inf')
    bestMove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)


def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(bot):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore


def main():
    global board
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

    printBoard(board)
    print("Computer goes first! Good luck.")
    print("Positions are as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("\n")

    while not checkForWin():
        compMove()
        if not checkForWin():
            playerMove()


player = 'O'
bot = 'X'
main()
