import random
import math
# functions go here

# Number checking function makes sure integer above 0 is entered
def num_check(question, error, low=None, high=None, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()

            
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
        
        elif response == "rps":
            response = "RPS"
            return response

        else:
            print("Please input yes / no")


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
# ask how many rounds user wants to play
rounds = num_check("How many rounds? ", "oops", 0, exit_code="")
print()

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
    # while rounds != rounds_played - 1:

        guesses_allowed = max_guesses

        

        # Already guessed list
        already_guessed = []
        

        # Normal Mode:
        # User inputs a highest and a lowest, and guesses, with limited tries
        
        while rounds_played < rounds:
            # randomizes the answer from the high and low numbers given
            ans = random.randint(lowest, highest)
            # gets answer in single variable
            secret = ans
            print()

            print("*** Round {} *****".format(rounds_played + 1))
            print("Spoiler Alert", secret)  # remove later

            if guess < lowest or guess > highest:
                print("Please enter a number between {} and {}".format(lowest, highest))
            
            else:

                # user inputs a guess, w/ error
                print()
                guess = num_check("Guess: ", "Please enter an integer between {} and {}".format(lowest, highest), exit_code="xxx")
                print()

                # checks that guess is not a duplicate
                if guess in already_guessed:
                    print("You have already guessed that number! Please try again.")
                    print("You *still* have {} guesses left".format(guesses_allowed))


                if rounds == rounds_played:
                    play_again = "no"
                    print("GAME OVER")
                    break


                # adds guess to list to prevent duplicate guesses
                already_guessed.append(guess)

                # Checks answer and compares it to hidden number
                if guesses_allowed >= 1 and guess != secret:                    

                    # quitting mechanism if user inputs xxx
                    if guess == "xxx":
                        play_again = "no"
                        print("You Quit")
                        break

                    # if the guess is less than the answer, tell them to try a higher num
                    if guess < secret:
                        print("**Too low, try a higher number**")
                        print()
                        guesses_allowed -= 1

                    # if the guess is higher than the answer, tell them to try a lower num
                    elif guess > secret:
                        print("**Too high, try a lower number**")
                        print()
                        guesses_allowed -= 1

                    # displays how many guesses user has left
                    print("Guesses Left: {}".format(guesses_allowed))

                else:
                    # if user runs out of guesses and final guess is lower than ans:
                    if guess < secret:
                        print("**Too low! Game Over!**")
                        print("Answer; {}".format(secret))
                        result = "lose"
                        rounds_played += 1
                        game_summary.append(result)
                        rounds_lost += 1
                        already_guessed.clear()
                        break
                    
                    # if user runs out of guesses and final guess is higher than ans:
                    elif guess > secret:
                        print("**Too high! Game Over!**")
                        print("Answer; {}".format(secret))
                        rounds_played += 1
                        result = "lose"
                        game_summary.append(result)
                        already_guessed.clear()
                        rounds_lost += 1
                        break

                
                # if user guesses ans, congatulatulate them and end game
                if guess == secret:
                    print("You got it right")
                    rounds_won += 1
                    print()
                    result = "win"
                    game_summary.append(result)
                    already_guessed.clear()
                    rounds_played += 1
                

        game_summary.append(result)

        # **** Calculate Game Stats ****
        percent_win = rounds_won / rounds_played * 100
        percent_lose = rounds_lost / rounds_played * 100

        # Asks user if they want to see there history
        show_history = yes_no("Would you like to see game history? ")

        # displays history if user says yes
        if show_history == "yes":
            print()
            print("**** Game History ****")
            for game in game_summary:
                print(game)



        # Doesnt display history if user says no
        elif show_history == "no":
            print()
            print("Thanks for Playing")

        # asks user if they want to see the game stats
        game_results = yes_no("Do you want to see your game stats? ")

        if game_results == "yes":

            # Displays game stats with % values to the nearest whole number
            print()
            print("**** Game Statistics ****")
            print("Win: {}: ({:.0f}%)\nLoss: {}: ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose))
            print()
            print()
            print("Thanks for playing")
            break
        elif game_results == "no":
            print()
            print("Thanks for playing")
            break
