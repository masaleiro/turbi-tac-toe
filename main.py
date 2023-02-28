#/usr/bin/python3

import pygame
import math


WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
BUTTON_RADIUS = WINDOW_HEIGHT/6-20

def playerPlay_gui(board, player, events, window):
    """
    Gets player input (mouse click) from the GUI

    Parameters
    ----------
    board : dict, required
    player : char, required
    events : list, required
    window : Surface, required

    Returns
    -------
    Bool, dict
    """
    button_positions = getGameButtonPositions(window)

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            button_idx = getPressedButton(button_positions)
            if validPlay(board, button_idx+1):
                board[button_idx+1] = player
                return True, board
    
    return False, board

def printBoard_gui(board, window, players, playerSymbols):
    """
    Prints the board in the pygame window

    Parameters
    ----------
    board : dict, required
    window : Surface, required
    players : list, required
    playerSymbols : dict, required 

    """
    window.fill((255,255,255))
    board_art = pygame.image.load("assets/board.png").convert()
    window.blit(board_art, (0,0))
    button_positions = getGameButtonPositions(window)
    for i in range(1,10):
        for player in players:
            if board[i] == player:
                position = (button_positions[i-1][0]-playerSymbols[player].get_rect().height/2,button_positions[i-1][1]-playerSymbols[player].get_rect().width/2)
                window.blit(playerSymbols[player], position)
    
    pygame.display.update()


def getGameButtonPositions(window):
    """
    Gets list of button positions

    Parameters
    ----------
    window : Surface, required

    Returns
    -------
    list
    """
    window_width, window_height = window.get_size()
    return [(x,y) for y in range(int(window_height/6),int(window_height),int(window_height/3)) for x in range(int(window_width/6),int(window_width),int(window_width/3))]


def loadSymbolDictionary_gui(players):
    """
    Loads the player images into a dictionary

    Parameters
    ----------
    players : list, required

    Returns
    -------
    dict
    """
    cross = pygame.image.load("assets/cross_white.png").convert()
    circle = pygame.image.load("assets/circle_white.png").convert()
    return {players[0]:cross,players[1]: circle}


def getMenuInput_gui(window):
    """
    Gets player input from the menu

    Parameters
    ----------
    window : Surface, required

    Returns
    -------
    Bool, char
    """
    window_width, window_height = window.get_size()
    button_positions = [(200,window_height/2),(505,window_width/2)]

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            button_idx = getPressedButton(button_positions)
            if button_idx == 0:
                return True, "S"
            elif button_idx == 1:
                return True, "Q"
    
    return False, ""

def printMenu_gui(board, window):
    """
    Prints the menu in the pygame window

    Parameters
    ----------
    board : dict, required    
    window : Surface, required
    """
    board = pygame.image.load("assets/menu.png").convert()
    window.blit(board, (0,0))
    pygame.display.update()


def getPressedButton(button_positions):
    """
    Gets which of the buttons was pressed

    Parameters
    ----------
    button_positions : list, required

    Returns
    -------
    int
    """
    coordinates = pygame.mouse.get_pos()
    print("Mouse click on coordinates ",coordinates)
    for idx, position in enumerate(button_positions):
        if euclideanDistance(coordinates, position) < BUTTON_RADIUS:
            print("You have pressed button number ", idx+1)
            return idx
    return -1


def euclideanDistance(pointA, pointB):
    """
    Calculates Euclidean Distance between two points

    Parameters
    ----------
    pointA : tuple, required
    pointB : tuple, required

    Returns
    -------
    float
    """
    dist = math.sqrt((pointA[0]-pointB[0])**2+(pointA[1]-pointB[1])**2)
    #print(dist)
    return dist


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
    playerSymbols = loadSymbolDictionary_gui(players)

    current_player = None

    board, current_player = setupGame(board, current_player, players)

    while(True):
        events = pygame.event.get()
        handleGeneralEvents(events)

        if current_state == "MENU":
            #option = input("Press S to start playing. Any other key to exit.").upper()
            printMenu_gui(board, window)
            valid_input = False
            valid_input, option = getMenuInput_gui(window)
            if valid_input:
                if option == "S":
                    printBoard_cli(board)
                    printBoard_gui(board, window, players, playerSymbols)
                    current_state = "GAME"
                else:
                    exit()

        elif current_state == "GAME":
            #board = playerPlay_cli(board, current_player)
            valid_play = False
            valid_play, board = playerPlay_gui(board, current_player, events, window)

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