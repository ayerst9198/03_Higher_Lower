# Higher Lower Fully Working Program
# Program should work but needs to be tested for usability

# import modules
import random
import math


# Check if user is entering an integer correctly.
def intcheck(question, low=None, high=None):

    # sets up an error messages
    if low is not None and high is not None:
        error = "❗ Please enter an integer between {} and {} ❗. ".format(low, high)
        "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "❗ Please enter an integer that is more than or equal to {} ❗".format(low)
    elif low is None and high is not None:
        error = "❗ Please enter an integer that is less than or equal to {} ❗".format(high)

    else:
        error = "❗ Please enter an integer ❗"
    while True:
        try:
            response = int(input(question))
            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response
        # prints error if user enters a value error
        except ValueError:
            print(error)
            continue


# statement generator
def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

keep_going = ""
while keep_going == "":
    # set up place holders
    num_won = 0
    num_lost = 0
    rounds_played = 0
    game_stats = []
    bold = "\033[1m"
    reset = "\033[0;0m"

    # Main routine
    print(bold, "⬆ Higher Lower Game ⬇", reset)
    print("In this game you will be asked to choose a", bold, "high", reset,
          "and a", bold, "low", reset, "number.")
    print("You will then need to guess numbers to try and find a secret number.")
    print("The secret number will be a number in between the high and low numbers that you chose.")
    print("But don't worry, there will be clues that give you hints to what the number is.")
    print("Play as many times as you like and try and beat your high score!")
    print()
    input("Press enter to begin ")
    print("------------------------------")
    low = intcheck("Choose a Low Number: ")
    high = intcheck("Choose a High Number: ", low + 1)
    scale = high - low + 1
    max_raw = math.log2(scale)  # finds maximum # of guesses using binary search
    max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
    max_guesses = max_upped + 1
    print("Your Max Number of Guesses: {}".format(max_guesses))
    rounds = intcheck("How many rounds? ")
    print()

    
    

    while rounds_played < rounds:
        secret = random.randint(low, high)
        guess = ""
        correct_guesses_left = max_guesses

        while guess != secret and correct_guesses_left > 1:
            print()
            # print round number
            print("Round {}".format(rounds_played + 1))
            # where the user guesses
            guess = intcheck("Guess: ")
            already_guessed = []
            
            # checks that guess is not a duplicate
            if guess in already_guessed:
                print("You have already guessed that number! Please try again. "
                      "You still have {} guesses left".format(correct_guesses_left))
                continue
            already_guessed.append(guess)
            correct_guesses_left -= 1

            if correct_guesses_left >= 1:

                if guess < secret:
                        hl_statement("Too low try a higher number. Guesses left: {}".format(correct_guesses_left - 1), "⬆")
                elif guess > secret:
                    hl_statement("Too high, try a lower number. Guesses left: {}".format(correct_guesses_left - 1), "⬇")
            else:
                if guess > secret:
                        print("Too low!")
                elif guess > secret:
                    print("Too high!")
        if guess == secret:
            if correct_guesses_left == max_guesses - 1:
                hl_statement("Amazing you got it in one guess!", "✨")
                num_won += 1

            else:
                print("✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
                print("Well done you got it in {} guesses".format(max_guesses - correct_guesses_left))
                num_won += 1
                print("✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
        else:
            print("Sorry - you lose this round as you have run out of guesses")
            num_lost += 1

        game_stats.append(max_guesses - correct_guesses_left)
        print("Won: {} \t | \t Lost: {}".format(num_won, num_lost))
        rounds_played += 1

    # print game outcomes
    print("*** Score for Each Round... ***")
    list_count = 1
    for item in game_stats:
        # indicates if game has been won or lost
        if item > max_guesses:
            status = "lost, ran out of guesses"
        else:
            status = "won"

        print("Round {}: {}".format(list_count, item))
        list_count += 1

    # Calculate statistics
    print("Game Stats", game_stats)
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats) / len(game_stats)
    # Print statistics
    print()
    print("*** Summary Statistics ***")
    print("Best: {}".format(best))
    print("Worst: {}".format(worst))
    print("Average: {:.2f}".format(average))

    # Keep going?
    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
#Farewell user
print("Thank you for playing. Goodbye")
