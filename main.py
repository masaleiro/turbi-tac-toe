#/usr/bin/python3

import pygame


WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

def initPygameWindow(width, height):
    """
    Initialize the Pygame window

    Parameters
    ----------
    width : int, required
    height: int, required

    Returns
    -------
    Surface
    """
    window = pygame.display.set_mode((width, height))
    return window

def initPygameWindow(width, height):
    """
    Initialize the Pygame window

    Parameters
    ----------
    width : int, required
    height: int, required

    Returns
    -------
    Surface
    """
    window = pygame.display.set_mode((width, height))
    return window

def handleGeneralEvents(events):
    """
    Function to handle general game events

    Parameters
    ----------
    events : list, required

    Returns
    -------
    list
    """    
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    return events


def winnerFound(board):
    """
    Analyzes the board to check if any player has won the game. 
    If a winner exists returns True. If not, returns False

    Parameters
    ----------
    board : dict, required

    Returns
    -------
    Bool
    """
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

    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    window = initPygameWindow(WINDOW_WIDTH,WINDOW_HEIGHT)


    # setup section
    previous_state = "SETUP"
    current_state = "MENU"
    board = None
    players = ['T', 'K']
    current_player = None

    board, current_player = setupGame(board, current_player, players)

    while(True):
        events = pygame.event.get()
        handleGeneralEvents(events)

        if current_state == "MENU":
            option = input("Press S to start playing. Any other key to exit.").upper()
            if option == "S":
                current_state = "GAME"
            else:
                exit()

        elif current_state == "GAME":
            printBoard_cli(board)
            board = playerPlay_cli(board, current_player)

            if winnerFound(board):
                    print("Player " + current_player + " won!")
                    current_state = "GAMEOVER"

            current_player = switchPlayer(players, current_player)

        elif current_state == "GAMEOVER":
            option = input("Press S to start again. Any other key to exit.").upper()
            if option == "S":
                print("Cool! Starting a new game!")
                board, current_player = setupGame(board, current_player, players)
                printBoard_cli(board)
                current_state = "GAME"
            else:
                exit()

        if current_state != previous_state:
            print("Switching from state "+ previous_state + " to " + current_state)
            previous_state = current_state