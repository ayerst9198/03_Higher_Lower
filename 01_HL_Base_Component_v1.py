import random
# functions go here

# Number checking function goes here
def num_check(question, error, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = int(input(question))

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


# Main routine
already_guessed = []
num_won = 0
lowest = num_check("Low Number: ", "Enter an integer above 0", 1)
highest = num_check("High Number: ", "Please enter a integer above {}".format(lowest), lowest + 1)
guesses_allowed = num_check("No. of Guesses: ", " Please enter an integer above 0", 0)
ans = random.randint(lowest, highest)
secret = ans
guess = ""
print(secret)
while guess != secret and guesses_allowed >= 1:

    guess = num_check("Guess:", "Please input a number between {} and {}".format(lowest, highest))    # Replace with function

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You have already guessed that number! Please try again.")
        print("You *still* have {} guesses left".format(guesses_allowed))
        continue

    guesses_allowed -= 1
    already_guessed.append(guess)

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
        print("You got it right")
        break

