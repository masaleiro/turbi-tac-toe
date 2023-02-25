#/usr/bin/python3

import pygame
import math

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
BUTTON_RADIUS = WINDOW_HEIGHT/6-20

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


def validPlay(board, play):
    if play in range(1,10) and board[play] in range(1,10):
        return True
    
    return False


def player_play_cli(board, player):
    play=-1
    while not validPlay(board, play):
        play = int(input("Player " + player + ", choose position to play from 1 to 9 "))
    board[play] = player


def euclideanDistance(pointA, pointB):
    dist = math.sqrt((pointA[0]-pointB[0])**2+(pointA[1]-pointB[1])**2)
    #print(dist)
    return dist


def getPressedButton(button_positions):
    coordinates = pygame.mouse.get_pos()
    print("Mouse click on coordinates ",coordinates)
    for idx, position in enumerate(button_positions):
        if euclideanDistance(coordinates, position) < BUTTON_RADIUS:
            print("You have pressed button number ", idx+1)
            return idx
    return -1


def player_play_gui(board, player, events, window):
    window_width, window_height = window.get_size()
    button_positions = [(x,y) for y in range(int(window_height/6),int(window_height),int(window_height/3)) for x in range(int(window_width/6),int(window_width),int(window_width/3))]

    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            button_idx = getPressedButton(button_positions)
            if validPlay(board, button_idx+1):
                board[button_idx+1] = player
                return True, board
    
    return False, board


def printBoard(board):
    for i in range(3):
        for j in range(1,4):
            print(str(board[i*3+j])+" ",end="")
        print("\n")


def setupGame(board, current_player, players):
    board = dict(zip(range(1, 10), range(1, 10)))
    current_player = players[0]
    return board, current_player


def handle_general_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    return events

def init_pygame_window(width, height):
    window = pygame.display.set_mode((width, height))
    return window


if __name__ == "__main__":

    print("Welcome to TurbiKreuzToe")

    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    window = init_pygame_window(WINDOW_WIDTH,WINDOW_HEIGHT)


    # setup section
    previous_state = "SETUP"
    current_state = "MENU"
    board = None
    current_player=None
 
    # create player symbols
    players = ['T', 'K']

    board, current_player = setupGame(board, current_player, players)

    while(True):
        events = pygame.event.get()
        handle_general_events(events)
        if current_state == "MENU":
            option = input("Press S to start playing. Any other key to exit.").upper()
            if option == "S":
                printBoard(board)
                current_state = "GAME"
            else:
                exit()

        elif current_state == "GAME":
            valid_play = False
            valid_play, board = player_play_gui(board, current_player, events, window)
            # player_play_cli(board, current_player)

            if valid_play:
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