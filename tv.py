# Author: Tharny Elilvannan
# Last Updated: April 05, 2024
# Purpose: Simulates a tv menu.
#          I did this in first-year based off a prompt for a computing 
#          final from Professor Sam Scott.

class TV:

    def __init__(self, on_off:bool, input:str):
        self.on_or_off = on_off
        self.input = input
        self.volume = 1
        self.channel = 1
        self.mute = False

    def on(self):
        self.on_or_off = True

    def off(self):
        try:
            if self.on_or_off == True:
                self.on_or_off = False
            else:
                raise Exception("TV is not on.")
        except Exception as e:
            print(e)


    def change_channel(self, increase_decrease):
        try:
            if self.on_or_off == True:
                if self.input == "Cable":
                    if self.channel > 0 and self.channel < 1000:
                        if increase_decrease == ("increase"):
                            self.channel += 1
                        else:
                            self.channel -= 1
                    elif self.channel == 0:
                        if increase_decrease == "increase":
                            self.channel += 1
                        else:
                            raise Exception("TV channel cannot be decreased.")
                    elif self.channel == 1000:
                        if increase_decrease == "decrease":
                            self.channel -= 1
                        else:
                            raise Exception("TV channel cannot be increased.")
                else:
                    raise Exception("TV is not set to cable.")
            else:
                raise Exception("TV is not on.")
        except Exception as e:
            print(e)

    def change_input(self, input):
        try:
            if self.on_or_off == True:
                self.input = input
            else:
                raise Exception("TV is not on.")
        except Exception as e:
            print(e)

    def change_volume(self, increase_decrease):
        try:
            if self.on_or_off == True:
                if self.volume > 0 and self.volume < 100:
                    if increase_decrease == "increase":
                        self.volume += 1
                    else:
                        self.volume -= 1
                elif self.volume == 0:
                    if increase_decrease == "increase":
                        self.volume += 1
                    else:
                        raise Exception("Volume cannot be decreased.")
                elif self.volume == 100:
                    if increase_decrease == "decrease":
                        self.volume -= 1
                    else:
                        raise Exception("Volume cannot be increased.")
                else:
                    raise Exception("Volume Out of Range")
            else:
                raise Exception("TV is not on.")
        except Exception as e:
            print(e)

    def change_mute(self, mute):
        try:
            if self.on_or_off == True:
                if mute == "on":
                    self.mute = True
                else:
                    self.mute = False
            else:
                raise Exception("TV is not on.")
        except Exception as e:
            print(e)

    def __str__(self):
        if self.on_or_off == False:
            status = "TV is off."
        else:
            status = "TV is ON. Volume " + str(self.volume)

            if self.mute == True:
                status = status + " (muted). Showing "
            else:
                status = status + " (not muted). Showing "

            status = status + self.input

            if self.input == "Cable":
                status = status + " Channel " + str(self.channel) + "."

        return status

def menu():
    samsung = TV(True, "Cable")

    print(samsung)

    option = int(input("Press 1 if you would like to turn the TV on.\nPress 2 if you would like to turn the TV off.\nPress 3 if you would like to "
                       "change the input.\nPress 4 if you would like to change the volume.\nPress 5 if you would like an update.\n"
                       "Press 6 if you would like to toggle mute.\nPress 7 if you would like to change the channel.\n"))

    again = "no"

    while again == "no":
        try:
            if option == 1:
                samsung.on_or_off = True
            elif option == 2:
                samsung.on_or_off = False
            elif option == 3:
                input_change = input("\nWhat would you like to change the input to? ")
                samsung.change_input(input_change)
            elif option == 4:
                volume_change = input("\nWould you like to increase or decrease the volume? ")
                samsung.change_volume(volume_change)
            elif option == 5:
                print(samsung)
            elif option == 6:
                mute_change = input("Would you like mute to be on or off? ")
                samsung.change_mute(mute_change)
            elif option == 7:
                channel_change = input("Would you like to increase or decrease the channel? ")
                samsung.change_channel(channel_change)
            else:
                raise Exception("Incorrect menu option.")
        except Exception as e:
            print(e)

        again = input("\nWould you like to exit the menu? ")

        if again == "no":
            option = int(input(
                "\nPress 1 if you would like to turn the TV on.\nPress 2 if you would like to turn the TV off.\nPress 3 if you would like to "
                "change the input.\nPress 4 if you would like to change the volume.\nPress 5 if you would like an update.\n"
                "Press 6 if you would like to toggle mute.\nPress 7 if you would like to change to change the channel.\n"))

menu()