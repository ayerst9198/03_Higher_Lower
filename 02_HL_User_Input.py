import random

# HL component 1 - Get and check user inpput

# To Do
# Check a lowest is an integer (any integer)
# Check that highest is more thn lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# check that guess is between lowest and highest (lower and upper bound)


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


start = ""
lowest = num_check("Low Number: ", "Enter an integer above 0", 1)
highest = num_check("High Number: ", "Please enter a integer above {}".format(lowest), lowest + 1)
rounds = num_check("No. of Round: ", " Please enter an integer above 0", 0)
ans = random.randint(lowest, highest)
print(ans)
rounds_played = 1
while start == "":
    print()
    print("Round: {}".format(rounds_played))
    guess = num_check("Guess: ", "Please enter an integer between {}, and {}".format(lowest, highest), lowest, highest)
    rounds_played += 1
    if guess == ans:
        print("program continues")
        start = "xxx"
