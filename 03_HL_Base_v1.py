import random
# functions go here


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
            print("<error> Unknown Answer "
                  "Detected. Please Input Yes/No")


#  simplifies instructions
def instructions():
    print("***how to play***")
    print()
    print("The rules go here")
    print()
    return ""


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
    
# Main routine goes here...

show_instructions = yes_no("Have you played my "
                           "game before? ")

if show_instructions == "no":
    instructions()

print("program continues")