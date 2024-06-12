# import libraries
import pandas
from datetime import date


# *** Functions go here ***


# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check(question, error, num_type):
    while True:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Checks that user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"

        elif response == "n" or response == "no":
            return "no"

        else:
            print("Please enter yes / no")


def instructions():
    print('''
**** Instructions ****
Intructions go here
    ''')


# checks that user hasn't input a blank response
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this cant be blank. Please try again")
        else:
            return response


def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal:
        response = input("What is your goal (eg $500 or 50%) ")

        # check if first character is $
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response [-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue


        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. "
                                 "ie {:.2f} dollars? ,"
                                 " y / n".format(amount, amount))

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Main routine goes here
print("==== Fund Raising Calculator ====\n")

want_instructions = yes_no("Do you want to see the instructions ? ")

if want_instructions == "yes":
    instructions()
