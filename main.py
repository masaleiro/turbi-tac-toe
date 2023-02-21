#/usr/bin/python3

def winnerFound(board):
    for i in range(1,10,3):
        if board[i] == board[i+1] == board[i+2] and board[i] not in range(1,10):
            print("Winner found!, Row ",i)
            return True
    for i in range(1,4):    
        if board[i] == board[i+3] == board[i+6] and board[i] not in range(1,10):
            print("Winner found, Column ",i)
            return True
    if (board[1] == board[5] == board[9] or board[3] == board[5] == board[7]) and board[5] not in range(1,10):
        print("Winner found!, diagonal")
        return True
    return False

def switchPlayer(players, current_player):
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]

    return current_player


def notValid(board, play):
    if play in range(1,10) and board[play] in range(1,10):
        return False
    else:
        return True


def player_play(board, player):
    play=-1
    while notValid(board, play):
        play = int(input("Player " + player + ", choose position to play from 1 to 9 "))
    board[play] = player


def printBoard(board):
    for i in range(3):
        for j in range(1,4):
            print(str(board[i*3+j])+" ",end="")
        print("\n")

def setupGame(board, current_player, players):
    board = dict(zip(range(1, 10), range(1, 10)))
    current_player = players[0]
    return board, current_player



if __name__ == "__main__":
    print("Welcome to TurbiKreuzToe")

    # setup section
    previous_state = "SETUP"
    current_state = "MENU"
    board = None
    current_player=None
 
    # create player symbols
    players = ['T', 'K']

    board, current_player = setupGame(board, current_player, players)

    while(True):

        if current_state == "MENU":
            option = input("Press S to start playing. Any other key to exit.").upper()
            if option == "S":
                printBoard(board)
                current_state = "GAME"
            else:
                exit()

        elif current_state == "GAME":
            player_play(board, current_player)
            printBoard(board)

            if winnerFound(board):
                print("Player " + current_player + " won!")
                current_state = "GAMEOVER"

            current_player = switchPlayer(players, current_player)

        elif current_state == "GAMEOVER":
            option = input("Press Y to play again. Any other key to exit.").upper()
            if option == "Y":
                print("Cool! Starting a new game!")
                board, current_player = setupGame(board, current_player, players)
                printBoard(board)
                current_state = "GAME"
            else:
                exit()

        if current_state != previous_state:
            print("Switching from state "+ previous_state + " to " + current_state)
            previous_state = current_state