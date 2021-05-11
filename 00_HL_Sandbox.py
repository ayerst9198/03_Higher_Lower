    
    # randomizes the answer from the high and low numbers given
    ans = random.randint(lowest, highest)
    # gets answer in single variable
    secret = ans

    if mode == 1:
        # ask how many rounds user wants to play
        rounds = num_check("How many rounds? ", "oops", 0, exit_code="")
        print()
    elif mode == 2:
        rounds = 'hi how are ya"

    while rounds != rounds_played - 1:
        

        guesses_allowed = max_guesses

        

        # Already guessed list
        already_guessed = []
        

        # Normal Mode:
        # User inputs a highest and a lowest, and guesses, with limited tries
        
        while rounds_played < rounds:
            
            print()

            print("*** Round {} *****".format(rounds_played + 1))
            print("Spoiler Alert", secret)  # remove later


            # user inputs a guess, w/ error
            print()
            guess = num_check("Guess: ", "Please enter an integer between {} and {}".format(lowest, highest), exit_code="xxx")
            print()
            
            if guess < lowest:
                print("Please enter a number between {} and {}".format(lowest, highest))
            elif guess > highest:
                print("Please enter a number between {} and {}".format(lowest, highest))
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
    
elif game_results == "no":
    print()
    print("Thanks for playing")