import random
import math
# functions go here

# Number checking function makes sure integer above 0 is entered
def num_check(question, error, low=None, high=None, exit_code=None, konami_code=None, impossible_mode=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()

            if response == exit_code or konami_code or impossible_mode:
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
        
        elif response == "rps":
            response = "RPS"
            return response

        else:
            print("Please input yes / no")


# Instructions
def instructions():
    statement_generator("How to play", "*", "?")
    print("Instructions")
    return ""


# Easter egg game inside easter egg game
def lucky_you():

    valid = False
    while not valid:
        import random


        # functions go here
        def statement_generator(statement, decoration):
            sides = decoration * 3

            statement = "{} {} {}".format(sides, statement, sides)
            top_bottom = decoration * len(statement)

            print(top_bottom)
            print(statement)
            print(top_bottom)

            return ""


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
                    print("I don't understand. "
                        "Stop acting smart and just input Yes or No")


        def cont():
            input("Enter anything to continue the Game :D")


        def instructions():
            statement_generator("How to Play", "*")
            print()
            print("The aim of the game is to make as much money as possible!")
            print()
            print("It costs $1 to start a round.")
            print()
            print("A random token will be generated from a unicorn, horse, donkey, or zebra:")
            print()
            print("Unicorns are worth $4.")
            print("If you get a Zebra or a Horse, you lose $0.50")
            print("Watch out for Donkeys!")
            print("If you get a Donkey, you lose $1!")
            print()
            print("When you run out of money; YOU LOSE")
            print()
            print("Enjoy!")
            print()
            cont()
            return ""


        def num_check(question, low, high):
            error = "Please enter a whole number between 1 and 10\n"

            valid = False
            while not valid:
                try:
                    # ask the question
                    response = int(input(question))
                    # if amount is too low / too high give
                    if low < response <= high:
                        return response

                    # output error
                    else:
                        print(error)
                except ValueError:
                    print(error)


        # Main routine goes here...
        statement_generator("Welcome to the Lucky Unicorn Game", "*")
        print()

        show_instructions = yes_no("Have you played this "
                                "game before? ")

        if show_instructions == "no":
            instructions()

        # Ask user how much they want to play with...
        statement_generator("START", "+")
        print()
        how_much = num_check("How much would you "
                            "like to play with between $1 and $10? ", 0, 10)
        balance = how_much

        rounds_played = 0
        play_again = input("Please press <Enter> to play... ").lower()
        while play_again == "":

            # increase # of rounds played
            rounds_played += 1

            # print round number
            print()
            statement_generator("Round #{}".format(rounds_played), "*")
            chosen_num = random.randint(1, 100)
            print()

            # Adjust balance

            # if the random # is between 1 and 5,
            # user gets a unicorn (add $4 to the balance)
            if 1 <= chosen_num <= 5:
                chosen = "unicorn"
                balance += 4

            # if the random # is between 6 and 36,
            # user gets a donkey (subtract $1 from balance)
            elif 6 <= chosen_num <= 36:
                chosen = "donkey"
                balance -= 1

            # token is either horse or zebra...
            # either way subtract $0.5 from balance
            else:
                # if the number is even, set the chosen
                # item to horse
                if chosen_num % 2 == 0:
                    chosen = "horse"
                # if the number is odd, set the chosen
                # item to zebra
                else:
                    chosen = "zebra"
                balance -= 0.5

            if chosen == "unicorn":
                statement_generator("You got a {}. Your balance is ${:.2f}".format(chosen, balance), "$")
                print()
            elif chosen == "horse":
                statement_generator("You got a {}. Your balance is ${:.2f}".format(chosen, balance), "-")
                print()
            elif chosen == "zebra":
                statement_generator("You got a {}. Your balance is ${:.2f}".format(chosen, balance), "%")
                print()
            elif chosen == "donkey":
                statement_generator("You got a {}. Your balance is ${:.2f}".format(chosen, balance), "^")
                print()
            else:
                play_again = "xxx"
                print("You have somehow broken my game.")
                print("This is an error message and the game will now shut down.")

            if balance < 1:
                play_again = "xxx"
                print("You have run out of money.")
                print(statement_generator("Game Over", "'"))
            else:
                play_again = input("Press <Enter> to play again "
                                "or 'xxx' to quit ")

        print()
        statement_generator("Final Results", "=")
        statement_generator("Final Balance: ${}".format(balance), ".")
        print("Thank you for playing")


# Easter Egg Game
def play_game():

    valid = False
    while not valid:
        import random
        # functions go here


        # makes statements look good P.S. I MADE THIS CODE
        def statement_generator(statement, left_side_decoration, top_decoration, bottom_decoration, right_side_decoration):

            left_sides = left_side_decoration * 3

            right_sides = right_side_decoration * 3

            statement = "{} {} {}".format(left_sides, statement, right_sides)

            top_bottom = top_decoration * len(statement)

            bottom_bottom = bottom_decoration * len(statement)

            print(top_bottom)
            print(statement)
            print(bottom_bottom)

            return ""
        
        


        #  simplifies instructions
        def instructions():
            statement_generator("How to play", "*", "?", "?", "*")
            print()
            print("Choose either a number of rounds or press <enter> for")
            print("  infinite mode, or i for infinite impossible mode")
            print()
            print("Then for each round, choose from rock")
            print("/ paper / scissors (or xxx to quit)")
            print("You can type r / p / s / x if you")
            print("don't want to type the entire word")
            print()
            print("The rules are...")
            print("- Rock beats scissors")
            print("- Scissors beats paper")
            print("- Paper beats rock")
            print()
            statement_generator("Have fun", "^", "*", "-", "*")
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
                
                elif response == "lucky you":
                    response = "LU"
                    return response

                else:
                    print("Please input yes / no")


        # checks rock, paper, or scissors
        def choice_checker(question, valid_list, error):

            valid = False
            while not valid:

                # Ask user for choice (and put choice in lowercase)
                response = input(question).lower()

                # iterates through list and if response is an item
                # in the list (or the first letter of an iten), the
                # full item name is returned

                for item in valid_list:
                    if response == item[0] or response == item:
                        return item

                # output error if item not in list
                print(error)
                print()


        # checks rounds or infinite
        def check_rounds():
            while True:
                response = input("How many rounds: ")

                round_error = "Please type either <enter> " \
                            "or an integer that is more than 0"
                if response != "":
                    try:
                        if response == "i":
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

        # Main routine goes here


        rounds_lost = 0
        rounds_drawn = 0
        rounds_played = 0
        result = "quitter"

        # Lists of valid responses

        yes_no_list = ["yes", "no"]
        rps_list = ["rock", "paper", "scissors", "xxx"]
        game_summary = []

        # welcome user
        statement_generator("Welcome to Rock Paper Scissors", "|", "^", "-", "|")
        print()

        # Asks user if they have played before.
        show_instructions = yes_no("Have you played my "
                                "game before? ")

        # If 'no' show instructions
        if show_instructions == "no":
            print()
            instructions()


        elif show_instructions == "LU":
            print()
            lucky_you()
            
        # Ask user for # of rounds, <enter> for infinite mode
        rounds = check_rounds()


        # ask user for # of rounds then loop
        end_game = "no"
        while end_game == "no":

            # Rounds heading

            # Check if Continuous or impossible

            print()
            if rounds == "":
                heading = statement_generator("Continuous Mode: Round {}".format(rounds_played + 1), "!", "!", "!", "!")

            elif rounds == "i":
                heading = statement_generator("Impossible Mode: Round {}".format(rounds_played + 1), "💀", "", "", "💀")


            else:
                heading = "Round {} of {}".format(rounds_played + 1, rounds)
                # End game if exit code is typed
                if rounds_played == "":
                    end_game = "yes"
                    statement_generator(heading, "*", "*", "*", "*")


            choose_instruction = "Please choose rock (r), paper " \
                                "(p), or scissors (s): "

            choose_error = "Please choose from rock / " \
                            "paper / scissors (or xxx to quit)"

            # Ask user for choice and check it's valid

            choose = choice_checker(choose_instruction, rps_list,
                                    choose_error)

            if choose == "xxx":
                break

            # get computer choice
            comp_choice = random.choice(rps_list[:-1])

            # compare choices
            if rounds == "i":
                if choose == "rock":
                    comp_choice = "paper"
                    result = "lose"
                elif choose == "paper":
                    comp_choice = "scissors"
                    result = "lose"

                else:
                    comp_choice = "paper"
                    result = "lose"

            else:
                if choose == comp_choice:
                    result = "tied"

                elif choose == "rock" and comp_choice == "paper":
                    result = "lose"

                elif choose == "paper" and comp_choice == "scissors":
                    result = "lose"

                elif choose == "scissors" and comp_choice == "rock":
                    result = "lose"

                else:
                    result = "win"

                if result == "lose":
                    rounds_lost += 1
                elif result == "tied":
                    rounds_drawn += 1

            # add result to list
            game_summary.append(result)

            #  End game if exit code is typed

            if result == "tied":
                feedback = " It's a tie "
            elif result == "lose":
                feedback = "You chose {} and com chose {} -  you {} ".format(choose, comp_choice, result)
            else:
                feedback = "You chose {} and com chose {} -  you {} ".format(choose, comp_choice, result)


            # rest of loop / game

            print(feedback)
            print()

            rounds_played += 1

            # end game if requested # of rounds has been played
            if rounds_played == rounds:
                break

        # Display Game Summary


        print("***** Summary *****")
        print("Won: {} \t|\t Lost: {} \t|\t Draw: "
            "{}".format(rounds_won, rounds_lost, rounds_drawn))
        print()
        print("Thank you for playing")

        # Ask user if they want to see their game history
        history = yes_no("Do you want to see your history? ")
        # If 'yes' show history
        if history == "yes":
            if result == "quitter":
                print()
                statement_generator("lol, you are a quitting loser", "😭", "", "", "😭")

            else:
                rounds_won = rounds_played - rounds_drawn - rounds_lost

                # calculate game stats
                percent_win = rounds_won / rounds_played * 100
                percent_lose = rounds_lost / rounds_played * 100
                percent_tie = rounds_drawn / rounds_played * 100

                print()
                statement_generator("***** Game History *****", "|", "*", "-", "|")
                for game in game_summary:
                    print(game)

                print()

                # displays game stats with % values to the nearest whole number
                statement_generator("Game Statistics", "*", "?", "-", "*")
                print("Win: {}, ({:.0f}%)\nLoss: {}, "
                    "({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost,
                                                            percent_lose, rounds_drawn, percent_tie))
                print("Thank you for playing")
        else:
            print("Thank you for playing")

# Main routine

# ask user if they have played before
show_instructions = yes_no("Have you played before? ")
print()

# if user inputs yes, program continues
if show_instructions == "yes":
    print("Program Continues")
# List for game summaey from RPS 
game_summary = []
# if user inputs no, show instructions
if show_instructions == "no":
    instructions()
    

# Easter egg
elif show_instructions == "RPS":
    RPS = "true"
    while RPS == "true":
        ask_game = yes_no("Do you want to play a game? " )
        if ask_game == "yes":
            play_game()
        elif ask_game == "no":
            RPS = "False"
            break
        

# Initial setup gets range
num_won = 0
print()
lowest = num_check("Low Number: ", "Enter an integer above 0", 1)

highest = num_check("High Number: ", "Please enter a integer above {}".format(lowest), lowest + 1)
print()

# asks for number of rounds
rounds_lost = 0
rounds_played = 0
rounds_won = 0
rounds = num_check("How many rounds? ", "oops", 0, exit_code="", konami_code="UpUpDownDownLeftRightLeftRightBAStart", impossible_mode="i")
print()
# list to hold user guesses and help prevent duplicates
already_guessed = []



# calculates maximum number of guesses based on binary search strategy
num_range = highest - lowest + 1
max_raw = math.log2(num_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1

print()

# loops the code
guess = ""
play_again = "yes"

# makes sure that user plays for specified amount of rounds
while play_again == "yes":
    # while rounds != rounds_played - 1:

        # randomizes the answer and prints ans for debug purposes
        ans = random.randint(lowest, highest)
        secret = ans

        guesses_allowed = max_guesses

        # Already guessed list
        already_guessed = []
        
        while guess != secret and guesses_allowed >= 1:
            # continuous mode (never ends)
            if rounds == "":
                # displays round banner
                print()
                print("*** Round {} *****".format(rounds_played + 1))
                print("Max Guesses: {}".format(max_guesses))
                print("Spoiler Alert", secret)
                
                

                guess_instruction ="Guess: "
                guess_error = "Please enter a number between {} and {}".format(lowest, highest)

                guess = num_check(guess_instruction, guess_error, lowest, highest, "xxx")

                # checks that guess is not a duplicate
                if guess in already_guessed:
                    print("You have already guessed that number! Please try again.")
                    print("You *still* have {} guesses left".format(guesses_allowed))
                    continue

                guesses_allowed -= 1

                # adds guess to list to prevent duplicate guesses
                already_guessed.append(guess)

                # Checks answer and compares it to hidden number

                # checks if you are allowed to guess
                if guesses_allowed >= 1:
                    # Quit Mechanism
                    if guess == "xxx":
                        print("You Quit")
                        play_again = "no"
                        result = "quit"
                        break

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
                        result = "lose"
                        rounds_played += 1
                        game_summary.append(result)
                        rounds_lost += 1
                        break
                    
                    # if user runs out of guesses and final guess is lower than ans:
                    elif guess > secret:
                        print("Too high! Game Over!")
                        print("Answer: {}".format(secret))
                        result = "lose"
                        rounds_played += 1
                        game_summary.append(result)
                        rounds_lost += 1
                        break

                # If user guesses correctlt, congratulate them, and loop
                if guess == secret:
                    print("You got it right")
                    ans = random.randint(lowest, highest)
                    print()
                    rounds_played += 1
                    secret = ans
                    result = "win"
                    game_summary.append(result)
                    rounds_won += 1
                    break

            # Easy mode (user is always right)

            # konami code easter egg (user is always right, and has infinite guesses)
            elif rounds == "upupdowndownleftrightleftrightbastart":

                # Easy mode heading 
                heading = statement_generator("konami mode guess {}".format(rounds_played), "$", "")

                # ask user for guess
                guess = num_check("Guess: ", "Please enter an integer between {} and {}".format(lowest, highest), exit_code="xxx")

                # Exit game if Exit code typed
                if guess == "xxx":
                    play_again = "no"
                    print("you quit lol")
                    result = "quit"
                    game_summary.append(result)
                    break
                
                # Allows user to always win
                secret = guess
                guesses_allowed = "9.99999999E x 10^99"

                print("You got it right")
                rounds_won += 1
                result = "win"
                game_summary.append(result)
                print("Guesses left", guesses_allowed)
                rounds_played += 1
            

            # Impossible mode easter egg makes user always wrong
            elif rounds == "i":
                heading = statement_generator("Impossible Mode: Guesses left: 1".format(rounds_played + 1), "x", "")
                
                # answer is a decimal so user will always be wrong
                secret = 1.5
                guess = num_check("Guess: ", "Please enter an integer between {} and {}".format(lowest, highest), exit_code="xxx")
                
                # quit mechanism when user inputs xxx
                if guess == "xxx":
                    play_again = "no"
                    print("you quit lol")
                    result = "quit"
                    game_summary.append(result)
                    break
                
                # losingh message
                print("you lose")
                result = "lose"
                game_summary.append(result)
                rounds_lost += 1
                rounds_played += 1

            # Normal Mode:
            # User inputs a highest and a lowest, and guesses, with limited tries
            else:
                while rounds_played < rounds:
                    print()
                    print("*** Round {} *****".format(rounds_played + 1))
                    print("Max Guesses: {}".format(max_guesses))
                    print("Spoiler Alert", secret)
                    # user inputs a guess, w/ error
                    guess = num_check("Guess: ", "Please enter an integer between {} and {}".format(lowest, highest), exit_code="xxx")

                    # checks that guess is not a duplicate
                    if guess in already_guessed:
                        print("You have already guessed that number! Please try again.")
                        print("You *still* have {} guesses left".format(guesses_allowed))
                        continue

                    if rounds == rounds_played + 1:
                        play_again = "no"
                        print("GAME OVER")
                        break

                    guesses_allowed -= 1

                    # adds guess to list to prevent duplicate guesses
                    already_guessed.append(guess)

                    # Checks answer and compares it to hidden number
                    if guesses_allowed >= 1:

                        # quitting mechanism if user inputs xxx
                        if guess == "xxx":
                            play_again = "no"
                            print("you quit lol")
                            break

                        # if the guess is less than the answer, tell them to try a higher num
                        if guess < secret:
                            print("Too low, try a higher number")
                            print()

                        # if the guess is higher than the answer, tell them to try a lower num
                        elif guess > secret:
                            print("Too high, try a lower number")
                            print()
                    else:
                        # if user runs out of guesses and final guess is lower than ans:
                        if guess < secret:
                            print("Too low! Game Over!")
                            print("Answer; {}".format(secret))
                            result = "lose"
                            rounds_played += 1
                            game_summary.append(result)
                            rounds_lost += 1
                            break
                        
                        # if user runs out of guesses and final guess is higher than ans:
                        elif guess > secret:
                            print("Too high! Game Over!")
                            print("Answer; {}".format(secret))
                            rounds_played += 1
                            result = "lose"
                            game_summary.append(result)
                            rounds_lost += 1
                            break

                    # displays how many guesses user has left
                    print("Guesses Left: {}".format(guesses_allowed))
                    rounds_played += 1
                    
                    # if user guesses ans, congatulatulate them and end game
                    if guess == secret:
                        print("You got it right")
                        rounds_won += 1
                        print()
                        result = "win"
                        game_summary.append(result)
                        rounds_played += 1
                        break

game_summary.append(result)

# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

# Asks user if they want to see there history
show_history = yes_no("would you like to see game history? ")

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
elif game_results == "no":
    print()
    print("Thanks for playing")
