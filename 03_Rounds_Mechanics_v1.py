# functions go here


# checks input is valid
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

# Main routine goes here

rounds_played = 0
choose_instruction = "Please choose a number between _ and _"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    if rounds_played == rounds:
        break

    # Rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
        print()

    print(heading)
    choose = int(input("{} or 'xxx' to "
                       "end: ".format(choose_instruction)))

    if choose == "xxx":
        break

    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1

print()
print("Thank you for playing")