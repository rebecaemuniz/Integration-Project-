"""Rebeca Muniz

This program helps the the user calculate the sale price of items they
purchase at the store, total how much they spent, and stops them from
going over the limit they had decided in the beginning. The program keeps
a running list that tells the user what exactly they bought and prints it
out at the end. It also runs through
some basic math problems as a warm up.

I received help with my program from Kamp Duong and referenced this
website https://www.w3schools.com/python/python_while_loops.asp, https://
www.w3schools.com/python/python_for_loops.asp and
https://www.w3schools.com/python/python_casting.asp for parts of my project
This function separates the the warm up math problems from the shopping
calculator portion.
"""


def run_introduction_section():
    """This function goes through a series of simple math problems. The first
    set calculate the area of a trapezoid by accepting the inputs of the
    lengths. The next part calculates the area of a square and then the final
    portion enters how much money will be dispensed and how much money will not
    be dispensed. If they answer correctly it tells them it is correct and if
    it tells them the correct answer.
    """
    print("Hello! Welcome to the Shopping trip calculator!")
    print("I'm going to warm up my math skills with some basic math problems.")
    print("\nLet me figure out the area of a trapezoid.")

    while True:
        try:
            first_length = int(input("Enter the first dimension: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    while True:
        try:
            second_length = int(input("Enter the second dimension: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    while True:
        try:
            height_of_trap = int(input("Enter the height of it: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    area_of_trapezoid = (first_length * second_length / 2) * height_of_trap

    # The * is multiplying a and b and the / is dividing by 2. The second * is
    # multiplying everything by h.
    print("The area is", area_of_trapezoid, "square feet.")
    print("\nNext up area of a square.")

    while True:
        try:
            square_length = int(input("Enter the length of the square: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    area_of_square = square_length ** 2
    # The ** is taking the length and multiplying the length by itself 2 times
    print("The area is", area_of_square, "square feet.")
    print(
        "\nFinally a person wants to take out $150 from an atm that dispenses "
        "only $20 bills.")

    while True:
        try:
            money_dispensed_guess = int(input("How much money will they be "
                                              "able to take out? Enter your "
                                              "guess: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # The // is taking the amount of 20s that can be taken by 150 and then
    # the * is multiplying that by 20
    money_dispensed = 150 // 20 * 20
    # The % is getting the remaining amount from dividing by 20
    money_did_not_get = 150 % 20 * 1
    if money_dispensed_guess == money_dispensed:
        print("You got it right!")
    else:
        print("Nope.\nThey will be able to take out $", money_dispensed)
    print("They will still be missing $", money_did_not_get)


def attach_list_of_purchases(list_of_purchases):
    """This function prints each item in a list of purchases.

    Args:
        list_of_purchases: List of items to print.
    """
    print("You bought these item(s): ")
    length_of_list = len(list_of_purchases)  # The len function is used to
    # count the number of items in the list.
    for item in range(0, length_of_list):  # This starts the list at item zero
        # until the end of the list
        print("- ", list_of_purchases[item])  


def calculate_shopping_trip():
    """This function collects user input and calculates the total spending for
    the shopping trip.

    :return:
    It returns the list of purchases.
    """
    print("\nI'm ready to go. I think it would be best if we got to know each"
          " other better.")
    print("Let's start with something simple.")
    user_name = input("Enter your name: ")
    print("Hello " + user_name + "!")  # This adds the username
    # input to the string
    print("I'm here to help make sure you don't overspend on your"
          " shopping spree.")

    while True:
        try:
            spending_limit = int(input("What's your spending limit for this "
                                       "trip? \nEnter it here: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("Now I'll know what to look out for.")
    amount_spent = 0.0

    exit_loop = False  # This establishes the loop is always false.
    list_of_purchases = []  # This makes the list for purchases empty at the
    # start of the loop
    # The loop I created will continue happening
    # until the spending limit drops below 5.
    # The >= is a shortcut to say greater than or equal to
    while spending_limit >= 5 and not exit_loop:  # Two factors to continue
        # loop are for the limit to be greater than or equal to 5 and not
        # false.

        while True:
            try:
                first_item = int(input("How much is the item you are going to "
                                       "purchase cost? \nEnter the amount "
                                       "here: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        type_of_item = input("What type of item is this? ")
        list_of_purchases.append(type_of_item)  # This grabs the input of the
        # of item and put it into the list.
        item_on_sale = input("Is it on sale? I can calculate the price.Enter "
                             "yes or no: ")

        new_price = 0
        if item_on_sale == "yes" or item_on_sale == "Yes":
            # If item is equal to yes it will go into the if statement.
            sale_percent = int(input(
                "Was the percent off 40, 50, or 60?"
                "\nEnter the percentage here: "))
            # This loop is to make sure the user enters
            # in one of the options I listed above.
            while sale_percent != 40 and sale_percent != 50 and \
                    sale_percent != 60:  # This checks to make sure the input
                # is 40, 50, or 60; if not they have to reenter an input.
                sale_percent = int(input(
                    "Invalid percent off."
                    "\nEnter a percent off of 40, 50, 60."))

            if sale_percent == 40:
                new_price = first_item - first_item * 0.4
                print("This item costs", format(new_price, '.2f'))
            elif sale_percent == 50:
                new_price = first_item - first_item * 0.5
                print("This item costs", format(new_price, '.2f'))
            elif sale_percent == 60:
                new_price = first_item - first_item * 0.6
                print("This item costs", format(new_price, '.2f'))
            else:
                print("Invalid percent off.")
        else:
            print("I'll just add it to our tab.")
            new_price = first_item

        if spending_limit >= new_price:
            # This subtracts the new price from the spending limit
            spending_limit = spending_limit - new_price
            # This shortcut += adds the new_price to the total amount_spent
            amount_spent += new_price
        else:
            print("You don't have enough money for that item.")
        print("This is your new balance:", format(spending_limit, '.2f'))
        answer = input("Do you want to enter more items? yes or no: ")

        while answer != "no" and answer != "No" and \
                answer != "yes" and answer != "Yes":
            answer = input("Please enter yes or no. ")

        if answer != "yes" or answer != "Yes":
            exit_loop = True  # This makes the the user exit the loop

    print("You spent a total of: $", amount_spent)
    print("That was a fun time helping you shop!")
    print("\nIt's time to check out now!")

    return list_of_purchases


def survey_enjoyment():
    """This function asks the user of they enjoyed using the program and
    accepts the answer of yes, Yes or YESSS. If they enter any of those
    responses they will get Woot as their response. Anything else will just
    say "Aww, that's too bad.
    """
    answer = input("Did you enjoy my program? ")
    if answer == "yes" or answer == "Yes" or answer == "YESSS!":
        print("Woot!")
    else:
        print("Aww, that's too bad. :(")


def main():
    """This function runs each of the other functions in this order and ends
    with see you next time print statement.
    """
    run_introduction_section()
    list_of_purchases = calculate_shopping_trip()
    attach_list_of_purchases(list_of_purchases)
    survey_enjoyment()


print("See you next time!")

main()
