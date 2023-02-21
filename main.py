#/usr/bin/python3

def switchPlayer(players, current_player):
    """
    Switches between the two players

    Parameters
    ----------
    players : list, required
    current_player : char, required

    Returns
    -------
    char
    """
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]

    return current_player


def validPlay(board, play):
    """
    Checks if the play was valid. Takes the current play and checks in the board if it is valid or not.
    If it is valid, returns True, Otherwise, returns False

    Parameters
    ----------
    board : dict, required
    play : char, required

    Returns
    -------
    Bool
    """
    if play in range(1,10) and board[play] in range(1,10):
        return True
    
    return False


def playerPlay_cli(board, player):
    """
    Gets input from the player in the CLI.

    Parameters
    ----------
    board : dict, required
    player : char, required

    Returns
    -------
    dict
    """
    play=-1
    while not validPlay(board, play):
        play = int(input("Player " + player + ", choose position to play from 1 to 9 "))
    board[play] = player
    return board


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
            board = playerPlay_cli(board, current_player)
            current_player = switchPlayer(players, current_player)

        elif current_state == "GAMEOVER":
            pass

        if current_state != previous_state:
            print("Switching from state "+ previous_state + " to " + current_state)
            previous_state = current_state