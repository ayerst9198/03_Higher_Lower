import random
import math
# functions go here

# Number checking function makes sure integer above 0 is entered
def num_check(question, error, low=None, high=None, exit_code=None):


    print("this is a number checker")

    print("Low: ", low * 4)

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
                if response >= 0:
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
    statement_generator("How to play", "*", "?")
    print("Welcome to Higher Lower.")
    print()
    print("The goal of this game is to find the correct number")
    print()
    print("You can choose the lowest boundary of guesses and highest boundary of guesses")
    return ""



# Main routine

# ask user if they have played before
show_instructions = yes_no("Have you played before? ")
print()

# List for game summaey from RPS 
game_summary = []
# if user inputs no, show instructions
if show_instructions == "no":
    instructions()
    
      
mode = mode_checker("Do you want to play mode 1 or mode 2? ", "PLease enter either '1' or '2'")


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


# list to hold user guesses and help prevent duplicates
already_guessed = []


# calculates maximum number of guesses based on binary search strategy
num_range = highest - lowest + 1
max_raw = math.log2(num_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1

# display how many guesses the user has
print("Max Guesses per round: {}".format(max_guesses))
print()

# loops the code
guess = ""
play_again = "yes"

# makes sure that user plays for specified amount of rounds
while play_again == "yes":
    
    # randomizes the answer from the high and low numbers given
    ans = random.randint(lowest, highest)
    # gets answer in single variable
    secret = ans

    if mode == 1:
        # ask how many rounds user wants to play
        rounds = num_check("How many rounds? ", "oops", 0, exit_code="")
        print()
    elif mode == 2:
        rounds = 5

    while rounds_played < rounds:
        print("Round {}".format(rounds_played + 1))
        play_again = input("Again? yes / no")

        if mode == 2:
            rounds += 1

        rounds_played += 1