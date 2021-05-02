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


# Main routine

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

chicken = 0

print()
guess = ""
play_again = "yes"
# makes sure that user plays for specified amount of rounds
while play_again == "yes":
    while rounds != rounds_played - 1:

        print()
        print("*** Round {} *****".format(rounds_played + 1))

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
                if guess == "xxx":
                    print("You Quit")
                    break
                if guesses_allowed >= 1:
                    if guess < secret:
                        print("Too low, try a higher number.   Guesses left: {}".format(guesses_allowed))

                    elif guess > secret:
                        print("Too high, try a lower number.   Guesses left; {}".format(guesses_allowed))
                else:
                    if guess < secret:
                        print("Too low! Game Over!")
                        print("Answer: {}".format(secret))
                    elif guess > secret:
                        print("Too high! Game Over!")
                        print("Answer: {}".format(secret))
                    break
                if guess == secret:
                    print("You got it right")
                    ans = random.randint(lowest, highest)
                    secret = ans
                    break
                if guess == "xxx":
                    print("You Quit")
                    break
            # Easy mode (user is always right)
            if rounds == "UpUpDownDownLeftRightLeftRightBAStart":
                heading = statement_generator("konami mode  \
                    guess {}".format(rounds_played), "$", "")
                guess = num_check("Guess: {}".format(guesses_allowed), "Please \
                    enter an integer between {} and {}".format(lowest, highest))
                secret = guess
                guesses_allowed = "infinity"

                print("You got it right")
                break
            
            # impossible mode
            elif rounds == "i":
                print("Max Guesses: {}".format(max_guesses))
                heading = statement_generator("Impossible Mode: Guesses \
                    left: 1".format(rounds_played + 1), "x", "")
                secret = 1.5
                guess = num_check("Guess: ".format(guesses_allowed), "Please \
                    enter an integer between {} and {}".format(lowest, highest))
                
                if guess == "xxx":
                    print("You Quit")
                    break

                print("you lose")
                while chicken == 0:
                    print("you suck " * 1000)
            # Normal Mode:
            else:
                print("Guesses Left: {}".format(guesses_allowed))
                guess = num_check("Guess: ".format(guesses_allowed), "Please \
                    enter an integer\
                         between {} and {}".format(lowest, highest))

                # checks that guess is not a duplicate
                if guess in already_guessed:
                    print("You have already guessed\
                         that number! Please try again.")
                    print("You *still* have {} guesses left")
                    continue

                guesses_allowed -= 1

                # adds guess to list to prevent duplicate guesses
                already_guessed.append(guess)

                # Checks answer and compares it to hidden number
                if guesses_allowed >= 1:
                    if guess < secret:
                        print("Too low, try a higher number.   Guesses left: {}".format(guesses_allowed))

                    elif guess > secret:
                        print("Too high, try a lower number.   Guesses left; {}".format(guesses_allowed))
                else:
                    if guess < secret:
                        print("Too low! Game Over!")
                        print("Answer; {}".format(secret))
                    elif guess > secret:
                        print("Too high! Game Over!")
                        print("Answer; {}".format(secret))
                if guess == secret:
                    print("You got it right")
                elif guess == "xxx":
                    print("You Quit")
                    break
                    break
