# --------------------------------------------------------
# Author: James Griffiths
# Date Created: Monday, 26th June 2019
# Version: 1.0
# Description:
#
# Exercises for Programmers: Challenge 7 Area of a room
#
# Prompt the user of width and length of a room in feet and inches
# Output the area in square feet
# Output the area in square meters
# --------------------------------------------------------


# Set a list for what a user might enter for meters or feet, return the unit in a standard form else reprompt for a unit
def unitIs(unit):
    feet = ['feet', 'f', '']
    meters = ['meters', 'meter', 'm']

    if unit in feet:
        unitChoice = "feet"
        return unitChoice

    elif unit in meters:
        unitChoice = "meters"
        return unitChoice

    else:
        unitChoice = unitIs(
            input("Please enter either 'feet' or 'meters'. Would you like to use feet or meters as a unit? "))
        return unitChoice


# Universal check to see if an input is numeric, use float as values may not be natural
def isANumber(unit):
    try:
        units = float(unit)
        if units > 0:
            return units
        else:
            units = isANumber(input("Please enter a positive number: "))
            return units
    except ValueError:
        units = isANumber(input("Please enter a number: "))
        return units


# --------------------------------------------------------


# Prompt user for what units they would like to use
unitChoice = unitIs(input("Would you like to use feet or meters as a unit? "))

if unitChoice == "feet":
    # Do everything in feet
    length = isANumber(input("What is the length of the room in feet? "))
    width = isANumber(input("What is the width of the room in feet? "))
    area = length * width
    print("The area is: " + str(area) + " square feet.")

    # Display the area in meters for fun
    areaInM = round((length * width) * 0.09290304, 2)
    print("You didn't want this, but the area is: " + str(areaInM) + " square meters.")

elif unitChoice == "meters":
    # Do everything in meters
    length = isANumber(input("What is the length of the room in meters? "))
    width = isANumber(input("What is the width of the room in meters? "))
    area = length * width
    print("The area is: " + str(area) + " square meters.")

    # Display the area in feet for fun
    areaInF = round((length * width) / 0.09290304, 2)
    print("You didn't want this, but the area is: " + str(areaInF) + " square feet.")
