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
    print(f'    Your score: {human_score:>3}')
    print(f'    AI\'s score: {ai_score:>3}')
    print('')


# We are going to create a dictionary named "win_combos". There will be 1 key in this dictionary for each action the
#     human of computer can take.
# In each key: value pair, the value will be a list! This list contains the strings for all actions that the
#     key action can beat. A list is defined by using square brackets "[" and "]", and has any number of items inside,
#     separated by commas.
# With just Rock, Paper, and Scissors, using a list may seem like overkill, but what if there are more options later?
win_combos = {
    "Rock": [your_code],  # todo <-- replace your_code with the name of the action that Rock beats
    # todo <-- Add additional items to this dictionary to reflect all of the possible matchups
}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Let's print out a simple introduction to our program!
    print('A simple Rock, Paper, Scissors implementation')
    print('by Thomas Carroll')
    print('2024-04-01')
    # Print a blank line to give some space in the output.
    print('')

    human_options_dictionary = {
        '1': 'Rock',
        '2': 'Paper',
        '3': 'Scissors',
    }

    # Let's tell the computer we are playing the game with a variable that is True while playing the game
    #     and False when it is time to end the game
    playing_game = True
    human_score = 0
    ai_score = 0

    # Tell the human what they can do
    print_options()

    # This is a while loop that will continue as long as we are playing. When playing_game becomes False, we will exit
    while playing_game:
        # Ask the human for their choice (paper, rock, or scissors), and store this in a variable
        human_choice = input('Your choice? ')

        # Decide what to do based on the human's choice
        if human_choice in human_options_dictionary:
            human_does = human_options_dictionary[human_choice]

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
                # If human_does != ai_does, then one of them must be a winner. We can compare each of their actions to
                #     the actions listed in the win_combos dictionary to see if a winning combination exists!
                # When we find out who won, we need to output a message to the console, and increase that player's score
                if your_code in win_combos[your_code]:  # todo <-- replace your_code to make this work
                    print("You win!")
                    your_code += 1  # todo <-- replace your_code to make this work
                elif your_code in win_combos[your_code]:  # todo <-- replace your_code to make this work
                    print("Computer wins!")
                    your_code += 1  # todo <-- replace your_code to make this work
                else:
                    print("This should never happen!")

            # Print out the scores after the end of every round
            print_score(human_score, ai_score)

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
