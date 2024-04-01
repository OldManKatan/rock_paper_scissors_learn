import random


your_code = ''


def print_options():
    # Print out the options that the player may choose
    pass


def get_opponent_pick():
    # Randomly choose one from "Rock", "Paper", or "Scissors", and return it
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Let's print out a simple introduction to our program!
    #     What is it?
    #     Who wrote it?
    #     When did you write this?
    your_code  # <-- Your code here

    # Print a blank line to give some space in the output.
    your_code  # <-- Your code here

    # Let's tell the computer we are playing the game with a variable that is True while playing the game
    #     and False when it is time to end the game
    # Name this variable playing_game
    playing_game = your_code  # todo <-- Your code here

    # This is a while loop that will continue as long as we are playing. When playing_game becomes False, we will exit
    while playing_game:
        # Tell the human what they can do by calling a the function print_options that you created above
        your_code  # todo <-- Your code here

        # Ask the human for their choice (Rock, Paper, or Scissors), and store this in a variable
        # The human will use "1" for Rock, "2" for Paper, and "3" for Scissors
        # HINT: Use the input('prompt') built in function to get the human input,
        #     store their answer in a variable called human_choice
        human_choice = your_code  # todo <-- Your code here

        # Decide what to do based on the human's choice
        # Our first if question asks whether the human gave us an input we know how to handle.
        # HINT: Did the human player enter "1" or "2" or "3"? Or something else?
        if your_code:  # todo <-- Replace the your_code with the conditional
            # Use an if, elif, elif to convert the player's number into one of the choices:
            # "Rock", "Paper", or "Scissors"; spelled exactly like this with the first letter capitalized.
            # Store the string "Rock", "Paper", or "Scissors" in a variable named human_does
            if human_choice == '1':
                human_does = your_code  # todo <-- Your code here
            elif human_choice == '2':
                human_does = your_code  # todo <-- Your code here
            elif human_choice == '3':
                human_does = your_code  # todo <-- Your code here
            else:
                print(f'human_choice = "{human_choice}" This should never happen!')
                continue

            # Print out what the human chose:
            your_code  # todo <-- Your code here

            # Figure out what the computer opponent is doing, and see who wins!
            # Use the get_opponent_pick function you defined above
            ai_does = your_code  # todo <-- Your code here

            # Print out what the computer chose using a print statement:
            your_code  # todo <-- Your code here

            # Let's compare the choices made by the human and the computer, and see who won!
            # The first case we want to check is if they both picked the same thing. This is a draw.
            # HINT: we want to compare the variables called "human_does" and "ai_does"
            if your_code:  # <-- Replace the your_code with the conditional
                # If it is a draw, then print a statement out saying this was a draw
                your_code  # todo <-- Your code here

            # Next, let's handle when someone wins
            else:
                if human_does == 'Rock':
                    if ai_does == your_code:  # todo <-- Replace the your_code with the conditional
                        print("You win!")
                    elif ai_does == your_code:  # todo <-- Replace the your_code with the conditional
                        print("Computer wins!")
                    else:
                        # just in case we missed something, let's print out a warning
                        print("This should never happen!")
                elif human_does == 'Paper':
                    if ai_does == your_code:  # todo <-- Replace the your_code with the conditional
                        print("You win!")
                    elif ai_does == your_code:  # todo <-- Replace the your_code with the conditional
                        print("Computer wins!")
                    else:
                        # just in case we missed something, let's print out a warning
                        print("This should never happen!")
                elif human_does == 'Scissors':
                    if ai_does == your_code:  # todo <-- Replace the your_code with the conditional
                        print("You win!")
                    elif ai_does == your_code:  # todo <-- Replace the your_code with the conditional
                        print("Computer wins!")
                    else:
                        # just in case we missed something, let's print out a warning
                        print("This should never happen!")

        else:
            # If the player enters anything else, it isn't a valid option we are ready to handle!!
            # Let's tell them what went wrong, and skip to the next round
            your_code  # todo <-- Your code here

    # If the while loop ends, the game is over and we can exit out
    # Let's thank the human for playing and let the program close
    print('Thank you for playing!')
    print('Good bye!')
