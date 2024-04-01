import random


your_code = ''


def print_options():
    # Print out the options that the player may choose
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissors')
    print('q - Quit')


def get_opponent_pick():
    # Randomly choose one from "Rock", "Paper", or "Scissors", and return it
    ai_options = ['Rock', 'Paper', 'Scissors']
    opponent_pick = random.choice(ai_options)
    return opponent_pick


def print_score(human_score, ai_score):
    # This function will output the current scores of the human player and the computer player
    # This function takes 2 arguments, "human_score" and "ai_score".
    # Arguments are variables from outside of the function that you want to use inside of a function!
    # The "f" before the quotes for a string is a special way to put variables into a string. We call them "f-strings"
    print(f'You: {your_code}')  # todo <-- Your code here
    print(f'AI:  {your_code}')  # todo <-- Your code here
    print('')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Let's print out a simple introduction to our program!
    print('A simple Rock, Paper, Scissors implementation')
    print('by Thomas Carroll')
    print('2024-04-01')
    # Print a blank line to give some space in the output.
    print('')

    # Let's tell the computer we are playing the game with a variable that is True while playing the game
    #     and False when it is time to end the game
    playing_game = True
    # When the game starts up, we need to set the starting scores.
    # What is a good value to start the game with?
    human_score = your_code  # todo <-- Your code here
    ai_score = your_code  # todo <-- Your code here

    # This is a while loop that will continue as long as we are playing. When playing_game becomes False, we will exit
    while playing_game:
        # Tell the human what they can do
        print_options()

        # Ask the human for their choice (paper, rock, or scissors), and store this in a variable
        human_choice = input('Your choice? ')

        # Decide what to do based on the human's choice
        if human_choice == '1' or human_choice == '2' or human_choice == '3':
            if human_choice == '1':
                human_does = 'Rock'
            elif human_choice == '2':
                human_does = 'Paper'
            elif human_choice == '3':
                human_does = 'Scissors'
            else:
                print(f'human_choice = "{human_choice}" This should never happen!')
                continue

            # Print out what the human chose:
            print(f'You chose {human_does}')

            # Figure out what the computer opponent is doing, and see who wins!
            ai_does = get_opponent_pick()
            # Print out what the computer chose:
            print(f'The computer chose {ai_does}')


            # Let's compare the choices made by the human and the computer, and see who won!
            # The first case we want to check is if they both picked the same thing. This is a draw.
            if human_does == ai_does:
                print("It's a draw!")
            # Next, let's handle when someone wins
            else:
                if human_does == 'Rock':
                    if ai_does == 'Scissors':
                        print("You win!")
                        # If the human won, we want to increase their score by one.
                        your_code  # todo <-- Your code here
                    elif ai_does == 'Paper':
                        print("Computer wins!")
                        # If the computer won, we want to increase their score by one.
                        your_code  # todo <-- Your code here
                    else:
                        # just in case we missed something, let's print out a warning
                        print("This should never happen!")
                elif human_does == 'Paper':
                    if ai_does == 'Rock':
                        print("You win!")
                        # If the human won, we want to increase their score by one.
                        your_code  # todo <-- Your code here
                    elif ai_does == 'Scissors':
                        print("Computer wins!")
                        # If the computer won, we want to increase their score by one.
                        your_code  # todo <-- Your code here
                    else:
                        # just in case we missed something, let's print out a warning
                        print("This should never happen!")
                elif human_does == 'Scissors':
                    if ai_does == 'Paper':
                        print("You win!")
                        # If the human won, we want to increase their score by one.
                        your_code  # todo <-- Your code here
                    elif ai_does == 'Rock':
                        print("Computer wins!")
                        # If the computer won, we want to increase their score by one.
                        your_code  # todo <-- Your code here
                    else:
                        # just in case we missed something, let's print out a warning
                        print("This should never happen!")

            # Print out the scores after the end of every round
            # Call your print_score function to print the scores out to the console. Remember that you need to pass in
            #     two arguments in the right order: human_score and ai_score
            your_code  # todo <-- Your code here

        elif human_choice == 'q':
            # If the human wants to quit the game, let's exit out
            playing_game = False
        else:
            # If the player enters anything else, it isn't a valid option we are ready to handle!!
            # Let's tell them what went wrong, and skip to the next round
            print(f'"{human_choice}" is not a valid option, try again!')

    # If the while loop ends, the game is over and we can exit out
    # Let's thank the human for playing and let the program close
    print('Thank you for playing!')
    print('Good bye!')
