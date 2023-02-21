#/usr/bin/python3

if __name__ == "__main__":
    print("Welcome to TurbiTacToe")

    # setup section
    previous_state = "SETUP"
    current_state = "MENU"

    while(True):

        if current_state == "MENU":
            option = input("Press S to start playing. Any other key to exit.")
            if option == "S" or option == "s":
                current_state = "GAME"
            else:
                exit()

        elif current_state == "GAME":
            pass

        elif current_state == "GAMEOVER":
            pass

        if current_state != previous_state:
            print("Switching from state "+ previous_state + " to " + current_state)
            previous_state = current_state