# functions go here

def user_choice(question):
    valid = False
    while not valid:
        response = int(input(question))
        error_num = "Please input a number between 1 and '???'"

        try:

            if response >= 1:
                print()
                return response
            elif response <= 1:
                print()
                return response
            else:
                print(error_num)

        except ValueError:
            error_num


user_choice("please input a thing")