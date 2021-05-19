import random
import math
# functions go here


# Number checking function makes sure integer above 0 is entered
def num_check(question, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()


            if response == exit_code:
                return response

            else:
                response = int(response)
 
            if low is not None and high is not None:
                if low <= response <= high:
                    return response
                else:
                    print(error)

                    print()
                    continue

            elif low is not None:
                if response >= low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif high is not None:
                if response <= high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# puts a decorative border around statements
def statement_generator(statement, side_decoration, top_bottom_decoration):


    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# confines answers to yes / no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please input yes / no")


# confines answer to either 1 or 2 for mode choice
def mode_checker(question, error):
    valid = False
    while not valid:
        try: 
            response = int(input(question))

            if response == 1:
                response = 1
                return response
            
            elif response == 2:
                response = 2
                return response
        
            else:
                print("Please enter either '1' or '2'")
        except ValueError:
            print(error)
            print()


# Instructions
def instructions():
    statement_generator("How to PLay", "*", "-")
    print()
    print(
        "In this game your goal is too guess the\n"
        "randomly generated number between a high and low or your choice\n"
        "\n"
        "There are 2 modes:\n"
        "\n"
        "Mode 1: Normal Mode\n"
        "Mode 2: Infinite Mode\n"
        "\n"
        "To quit, you can input xxx to exit game\n"
        "at anytime while guessing."
    )
    return""


# Main routine
# Welocomes User
statement_generator("Welcome to Higher Lower", "-", "=")

# ask user if they have played before
show_instructions = yes_no("Have you played before? ")
print()

# List for game summaey from RPS
game_summary = []
# if user inputs no, show instructions
if show_instructions == "no":
    instructions()
    print()
    
      
mode = mode_checker(
    "Do you want to play mode 1 (normal mode), \n"
    "or mode 2 (infinite mode)? ", "PLease enter either '1' or '2'"
)


# Initial setup gets range
num_won = 0
print()
lowest = num_check("Low Number: ", "Enter an integer above 0", 1)

highest = num_check("High Number: ", "Please enter a integer above {}".format(lowest), lowest + 1)
print()

# set up rounds variables
rounds_lost = 0
rounds_played = 0
rounds_won = 0

# Gets number of rounds
if mode == 1:
    # ask how many rounds user wants to play
    rounds_allowed = num_check("How many rounds? ", "Please enter an integer above 0", 1, exit_code="")
    rounds = rounds_allowed
    print()
elif mode == 2:
    rounds_allowed = 5
    rounds = rounds_allowed

# list to hold user guesses and help prevent duplicates
already_guessed = []

# calculates maximum number of guesses based on binary search strategy
num_range = highest - lowest + 1
max_raw = math.log2(num_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1
guesses_allowed = max_guesses

# display how many guesses the user has
statement_generator("Max Guesses per round: {}".format(max_guesses), "-", "")


# loops the code
guess = ""
play_again = "yes"

# makes sure that user plays for specified amount of rounds
while play_again == "yes":
    rounds = rounds_allowed
    guess = 10000000
    while rounds_played < rounds:

        guesses_allowed = max_guesses

        # randomizes the answer from the high and low numbers given
        secret = random.randint(lowest, highest) 
        
        if mode == 2:
            rounds += 1

        statement_generator(" Round {} ".format(rounds_played + 1), "*", "*")

        #  ask user to guess and loop until they are correct / lose
        while guess != secret: 
            # user inputs a guess, w/ error
            
            guess = num_check("Guess: ", "Please enter an integer between {} and {}".format(lowest, highest), exit_code="xxx")
            print()

            # quitting mechanism if user inputs xxx
            if guess == "xxx":
                rounds = rounds_played - 1
                statement_generator("You Quit", "-", "")
                print()
                break
            
            if guess != secret:
                if guess < lowest:
                    guesses_allowed += 1
                    print("Please enter a number between {} and {}, or 'xxx' to quit".format(lowest, highest))
                    continue
                if guess > highest:
                    guesses_allowed += 1
                    print("Please enter a number between {} and {}, or 'xxx' to quit".format(lowest, highest))
                    continue
                # checks that guess is not a duplicate
                if guess in already_guessed:
                    print("You have already guessed that number! Please try again.")
                    print("You *still* have {} guesses left".format(guesses_allowed))
                    guesses_allowed += 1
                


            if rounds == rounds_played:
                
                rounds = rounds_played
                
                statement_generator("GAME OVER", "-", "")
                break


            # adds guess to list to prevent duplicate guesses
            already_guessed.append(guess)

            # Checks answer and compares it to hidden number
            if guesses_allowed >= 2 and guess != secret:                    

                

                # if the guess is less than the answer, tell them to try a higher num
                if guess < secret:
                    statement_generator("Too low, try a higher number", "*", "")
                    print()
                    guesses_allowed -= 1

                # if the guess is higher than the answer, tell them to try a lower num
                elif guess > secret:
                    statement_generator("Too high, try a lower number", "*", "")
                    print()
                    guesses_allowed -= 1

                # displays how many guesses user has left
                statement_generator("Guesses Left: {}".format(guesses_allowed), "", "-")

            else:
                # if user runs out of guesses and final guess is lower than ans:
                if guess < secret:
                    statement_generator("Too low! Game Over!", "*", "")
                    print("Answer; {}".format(secret))
                    result = "lose"
                    game_summary.append(result)
                    rounds_lost += 1
                    rounds_played += 1
                    already_guessed.clear()
                    break
                
                # if user runs out of guesses and final guess is higher than ans:
                elif guess > secret:
                    statement_generator("Too high! Game Over!", "*", "")
                    print("Answer; {}".format(secret))
                    result = "lose"
                    game_summary.append(result)
                    already_guessed.clear()
                    rounds_lost += 1
                    rounds_played += 1
                    break

            
                # if user guesses ans, congatulatulate them and end game
                elif guess == secret:
                    statement_generator("You got it right", "!", "-")
                    rounds_won += 1
                    print()
                    result = "win"
                    game_summary.append(result)
                    already_guessed.clear()
                    rounds_played += 1
        


    # **** Calculate Game Stats ****
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100
    print()
    print(rounds_won)
    print(rounds_played)
    print(rounds_lost)
    print(percent_lose)
    print(percent_win)
    print()

    # Asks user if they want to see there history
    show_history = yes_no("Would you like to see game history? ")

    # displays history if user says yes
    if show_history == "yes":
        print()
        statement_generator("Game History", "*", "*")
        for game in game_summary:
            print()
            print(game)
            print()



    # Doesnt display history if user says no
    elif show_history == "no":
        print()
        statement_generator("Thanks for Playing", "-", "*")

    # asks user if they want to see the game stats
    game_results = yes_no("Do you want to see your game stats? ")

    if game_results == "yes":

        # Displays game stats with % values to the nearest whole number
        print()
        statement_generator(" Game Statistics ", "+", "-")
        print("Win: {}: ({:.0f}%)\nLoss: {}: ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose))
        print()
        print()
        print("Thanks for playing")
        
    elif game_results == "no":
        statement_generator("Thanks for Playing", "-", "*")
    statement_generator("", "", "")

    # Asks user if they want to play again
    play_again = yes_no("Do you want to play again? ")

    if play_again == "yes":
        continue
    else:
        break