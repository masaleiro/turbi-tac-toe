#/usr/bin/python3

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


if __name__ == "__main__":
    print("Welcome to TurbiTacToe")

    # setup section
    previous_state = "SETUP"
    current_state = "MENU"

    # create game board
    board = dict(zip(range(1, 10), range(1, 10)))
    
    # create player symbols
    players = ['X', 'O']
    current_player = players[0]


    while(True):

        if current_state == "MENU":
            option = input("Press S to start playing. Any other key to exit.")
            if option == "S" or option == "s":
                current_state = "GAME"
            else:
                exit()

        elif current_state == "GAME":
            printBoard(board)
            player_play(board, current_player)
            
            current_player = switchPlayer(players, current_player)

        elif current_state == "GAMEOVER":
            pass

        if current_state != previous_state:
            print("Switching from state "+ previous_state + " to " + current_state)
            previous_state = current_state