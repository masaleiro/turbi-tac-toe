#/usr/bin/python3

def printBoard_cli(board):
    """
    Prints the board in the command line

    Parameters
    ----------
    board : dict, required
    """
    for i in range(3):
        for j in range(1,4):
            print(str(board[i*3+j])+" ",end="")
        print("\n")

def setupGame(board, current_player, players):
    """
    Function to setup game variables like the board and the starting player

    Parameters
    ----------
    board : dict, required
    players : list, required
    current_player : char, required

    Returns
    -------
    list
    """ 
    board = dict(zip(range(1, 10), range(1, 10)))
    current_player = players[0]
    return board, current_player


if __name__ == "__main__":
    print("Welcome to TurbiTacToe")

    # setup section
    previous_state = "SETUP"
    current_state = "MENU"
    board = None
    players = ['T', 'K']
    current_player = None

    board, current_player = setupGame(board, current_player, players)

    while(True):

        if current_state == "MENU":
            option = input("Press S to start playing. Any other key to exit.").upper()
            if option == "S":
                current_state = "GAME"
            else:
                exit()

        elif current_state == "GAME":
            printBoard_cli(board)
            input()
            pass

        elif current_state == "GAMEOVER":
            pass

        if current_state != previous_state:
            print("Switching from state "+ previous_state + " to " + current_state)
            previous_state = current_state