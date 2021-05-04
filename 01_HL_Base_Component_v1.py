import random
import math
# functions go here

# Number checking function makes sure integer above 0 is entered
def num_check(question, error, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()

            if response == "xxx":
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

# checks how many rounds the user wants to play
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                if response == "UpUpDownDownLeftRightLeftRightBAStart":
                    return response
                elif response == "i":
                    return response
                else:
                    response = int(response)
                
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


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


# Instructions
def instructions():
    statement_generator("How to play", "*", "?")
    print("Instructions")
    return ""

# Main routine

# ask user if they have played before
show_instructions = yes_no("Have you played before? ")

# if user inputs yes, program continues
if show_instructions == "yes":
    print("Program Continues")

# if user inputs no, show instructions
elif show_instructions == "no":
    instructions()

# asks for number of rounds
rounds_lost = 0
rounds_drawn = 0
rounds_played = 0
rounds = check_rounds()
# list to hold user guesses and help prevent duplicates
already_guessed = []

# Initial setup gets range
num_won = 0
lowest = num_check("Low Number: ", "Enter an integer above 0", 1)
highest = num_check("High Number: ", "Please enter a integer above {}".format(lowest), lowest + 1)

# calculates maximum number of guesses based on binary search strategy
range = highest - lowest + 1
max_raw = math.log2(range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1

# secret variable used for impossible mode
chicken = 0

print()

# loops the code
guess = ""
play_again = "yes"

# makes sure that user plays for specified amount of rounds
while play_again == "yes":
    while rounds != rounds_played - 1:
        
        # displays round banner
        print()
        print("*** Round {} *****".format(rounds_played + 1))

        # randomizes the answer and prints ans for debug purposes
        ans = random.randint(lowest, highest)
        secret = ans
        print("Spoiler Alert", secret)
        guesses_allowed = max_guesses
        
        while guess != secret and guesses_allowed >= 1:

            # continuous mode (never ends)
            if rounds == "":
                print("Max Guesses: {}".format(max_guesses))
                already_guessed = []

                guess = num_check("Guess: ".format(guesses_allowed), "Please enter an integer between {} and {}".format(lowest, highest))

                # checks that guess is not a duplicate
                if guess in already_guessed:
                    print("You have already guessed that number! Please try again.")
                    print("You *still* have {} guesses left".format(guesses_allowed))
                    continue

                guesses_allowed -= 1

                # adds guess to list to prevent duplicate guesses
                already_guessed.append(guess)

                # Checks answer and compares it to hidden number

                # Quit Mechanism
                if guess == "xxx":
                    print("You Quit")
                    play_again = "no"
                    break

                # checks if you are allowed to guess
                if guesses_allowed >= 1:

                    # if the guess is less than the answer, tell them to try a higher num
                    if guess < secret:
                        print("Too low, try a higher number.   Guesses left: {}".format(guesses_allowed))

                    # if guess is higher than ans, tell user to choose lower num
                    elif guess > secret:
                        print("Too high, try a lower number.   Guesses left; {}".format(guesses_allowed))

                # if user has no answer left:
                else:

                    # if user runs out of guesses and final guess is lower than ans: 
                    if guess < secret:
                        print("Too low! Game Over!")
                        print("Answer: {}".format(secret))
                        break
                    
                    # if user runs out of guesses and final guess is lower than ans:
                    elif guess > secret:
                        print("Too high! Game Over!")
                        print("Answer: {}".format(secret))
                        break

                # If user guesses correctlt, congratulate them, and loop
                if guess == secret:
                    print("You got it right")
                    ans = random.randint(lowest, highest)
                    print()
                    rounds_played += 1
                    secret = ans
                    break

            # Easy mode (user is always right)

            # konami code easter egg (user is always right, and has infinite guesses)
            if rounds == "UpUpDownDownLeftRightLeftRightBAStart":
                heading = statement_generator("konami mode guess {}".format(rounds_played), "$", "")
                guess = num_check("Guess: {}".format(guesses_allowed), "Please enter an integer between {} and {}".format(lowest, highest))
                secret = guess
                guesses_allowed = "infinity"

                print("You got it right")
                break
            
            # impossible mode

            # impossible mode easter egg makes user always wrong
            elif rounds == "i":
                print("Max Guesses: {}".format(max_guesses))
                heading = statement_generator("Impossible Mode: Guesses left: 1".format(rounds_played + 1), "x", "")
                
                # answer is a decimal so user will always be wrong
                secret = 1.5
                guess = num_check("Guess: ".format(guesses_allowed), "Please enter an integer between {} and {}".format(lowest, highest))
                
                # quit mechanism when user inputs xxx
                if guess == "xxx":
                    print("You Quit")
                    break
                
                # losingh message
                print("you lose")
                while chicken == 0:
                    print("you suck " * 1000)

            # Normal Mode:

            # User inputs a highest and a lowest, and guesses, with limited tries
            else:

                # displays how many guesses user has left
                print("Guesses Left: {}".format(guesses_allowed))

                # user inputs a guess, w/ error
                guess = num_check("Guess: ".format(guesses_allowed), "Please enter an integer between {} and {}".format(lowest, highest))

                # checks that guess is not a duplicate
                if guess in already_guessed:
                    print("You have already guessed that number! Please try again.")
                    print("You *still* have {} guesses left".format(guesses_allowed))
                    continue

                guesses_allowed -= 1

                # adds guess to list to prevent duplicate guesses
                already_guessed.append(guess)

                # Checks answer and compares it to hidden number
                if guesses_allowed >= 1:

                     # if the guess is less than the answer, tell them to try a higher num
                    if guess < secret:
                        print("Too low, try a higher number.   Guesses left: {}".format(guesses_allowed))
                        print()

                     # if the guess is higher than the answer, tell them to try a lower num
                    elif guess > secret:
                        print("Too high, try a lower number.   Guesses left; {}".format(guesses_allowed))
                        print()
                else:

                    # if user runs out of guesses and final guess is lower than ans:
                    if guess < secret:
                        print("Too low! Game Over!")
                        print("Answer; {}".format(secret))
                        print()
                    
                    # if user runs out of guesses and final guess is higher than ans:
                    elif guess > secret:
                        print("Too high! Game Over!")
                        print("Answer; {}".format(secret))
                        print()
                
                # if user guesses ans, congatulatulate them and end game
                if guess == secret:
                    print("You got it right")
                    print()
                    break
                
                # quitting mechanism if user inputs xxx
                elif guess == "xxx":
                    print("You Quit")
                    print()
                    break
