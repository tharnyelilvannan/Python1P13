# Author: Tharny Elilvannan
# Last Updated: October 25, 2024
# Purpose: Simulates a telephone menu for a restaurant.

done = False

while (done == False):
    selectionStr = input("1 - Make a reservation\n2 - Order takeout\n3 - Ask about our menu\nEnter your selection: ")
    selection = int(selectionStr)

    if (selection == 1):
        reservationDate = input("Enter a date: ")
        reservationTime = input("Enter a time: ")
        print("Your reservation has been made for " + reservationDate + " at " + reservationTime + ".")
    elif (selection == 2):
        order = input("Enter your order: ")
        print("Your order is " + order + ".")
    elif (selection == 3):
        menuTimeStr = input("Press 1 to ask about our Lunch menu.\nPress 2 to ask about our Dinner menu.\n")
        menuTime = int(menuTimeStr)

        if (menuTime == 1):
            print("LUNCH\nVegan Burger\nMargherita Pizza\nBeef Burger")
        elif (menuTime == 2):
            print("DINNER\nButternut Squash Ravioli with Cream Sauce\nChicken Parmesan\nSalmon with Mashed Potatoes")
        else:
            print("Error")
    else:
        print("Error")

    doneStatus = input("Would you like to go back to the main menu? Press y for yes. Press n for no. ")

    if (doneStatus == "n"):
        done = True