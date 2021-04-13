# HL Component 3 - no duplicates

# To Do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL component 3 - prevents duplicate guesses

secret = 7
guesses_allowed = 5

already_guessed = []
num_won = 0

guess = ""

# loops until you run out of guesses or number is correctly guessed
while guess != secret and guesses_allowed >= 1:

    guess = int(input("Guess:"))    # Replace with function

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You have already guessed that number! Please try again.")
        print("You *still* have {} guesses left".format(guesses_allowed))
        continue

    # Guess is not a duplicate, it gets counted and 
    # added to the list of numbers that have been guessed
    guesses_allowed -= 1
    already_guessed.append(guess)

    # If guess is too low, tells user to try a higher number
    if guesses_allowed >= 1:
        if guess < secret:
            print("Too low, try a higher number.   Guesses left: {}".format(guesses_allowed))

        elif guess > secret:
            print("Too high, try a lower number.   Guesses left; {}".format(guesses_allowed))
    else:
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")

if guess == secret:
    print("Good Job. You got it right.")
