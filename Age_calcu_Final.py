from random import choice
import time

def design():
    print("""
      ___   _____  _____   _____   ___   _      _____  _   _  _       ___  _____  _____ ______
     / _ \ |  __ \|  ___| /  __ \ / _ \ | |    /  __ \| | | || |     / _ \|_   _||  _  || ___ \\
    / /_\ \| |  \/| |__   | /  \// /_\ \| |    | /  \/| | | || |    / /_\ \ | |  | | | || |_/ /
    |  _  || | __ |  __|  | |    |  _  || |    | |    | | | || |    |  _  | | |  | | | ||    /
    | | | || |_\ \| |___  | \__/\| | | || |____| \__/\| |_| || |____| | | | | |  \ \_/ /| |\ \\
    \_| |_/ \____/\____/   \____/\_| |_/\_____/ \____/ \___/ \_____/\_| |_/ \_/   \___/ \_| \_|\n
    _________________________________Clarence M. Sarmiento_____________________________________\n""")

def prediction():
    words = ["You're going to die 6 years from now.", "You're going to die 3 weeks from now.",
             "You're going to die tomorrow.",  "You're dead from the inside.", "You're alive but not living.",
             "You're not having a family."]
    death_choice = choice(words)
    return death_choice

# Convert Birth Month to corresponding integers...
def month_of_birth(birth_month):
    # Check the month if available...
    if birth_month == "Jan" or birth_month == "January":
        x = 1
        return x
    elif birth_month == "Feb" or birth_month == "February":
        x = 2
        return x
    elif birth_month == "March":
        x = 3
        return x
    elif birth_month == "April":
        x = 4
        return x
    elif birth_month == "May":
        x = 5
        return x
    elif birth_month == "June":
        x = 6
        return x
    elif birth_month == "July":
        x = 7
        return x
    elif birth_month == "Aug" or birth_month == "August":
        x = 8
        return x
    elif birth_month == "Sept" or birth_month == "September":
        x = 9
        return x
    elif birth_month == "Oct" or birth_month == "October":
        x = 10
        return x
    elif birth_month == "Nov" or birth_month == "November":
        x = 11
        return x
    elif birth_month == "Dec" or birth_month == "December":
        x = 12
        return x
    else:
        print("Invalid Birth month")
        exit()
        return

# Covert Recent Month to corresponding integers...
def todays_month(recent_month):
    # Check the month if available...
    if recent_month == "January" or recent_month == "Jan":
        y = 1
        return y
    elif recent_month == "February" or recent_month == "Feb":
        y = 2
        return y
    elif recent_month == "March":
        y = 3
        return y
    elif recent_month == "April":
        y = 4
        return y
    elif recent_month == "May":
        y = 5
        return y
    elif recent_month == "June":
        y = 6
        return y
    elif recent_month == "July":
        y = 7
        return y
    elif recent_month == "August" or recent_month == "Aug":
        y = 8
        return y
    elif recent_month == "September" or recent_month == "Sep":
        y = 9
        return y
    elif recent_month == "October" or recent_month == "Oct":
        y = 10
        return y
    elif recent_month == "November" or recent_month == "Nov":
        y = 11
        return y
    elif recent_month == "December" or recent_month == "Dec":
        y = 12
        return y
    else:
        print("Invalid today's month")
        exit()
        return

# Search for what day of the year you're born...
def dayOfYear(year, month, day):
    if month == 1:
        month += 12
        year -= 1
    elif month == 2:
        month += 12
        year -= 1
    cent = (year // 100)
    cent_year = (year % 100)
    day_of_the_week = (day + ((26 * (month + 1)) // (10)) + cent_year + ((cent_year) // (4)) + ((cent) // (4)) + (
            5 * cent)) % 7
    if day_of_the_week == 0:
        return "Day you're born is Saturday."
    elif day_of_the_week == 1:
        return "Day you're born is Sunday."
    elif day_of_the_week == 2:
        return "Day you're born is Monday."
    elif day_of_the_week == 3:
        return "Day you're born is Tuesday."
    elif day_of_the_week == 4:
        return "Day you're born is Wednesday."
    elif day_of_the_week == 5:
         return "Day you're born is Thursday."
    elif day_of_the_week == 6:
        return "Day you're born is Friday."

# Convert your age to year...
def age_to_year(birth_year, age):
    year = birth_year + age
    return year

def do_you(birth_year):
    print("""Do you want to know what year you are going to be in a certain age
or what year do you want to have a family or something else?
Type 'x' to stop or any key to continue.""")
    response = input("=> ")
    response = response.lower()
    if response != "x":
        age = input("Enter age.\n=> ")
        print("It's going to be", age_to_year(birth_year=int(birth_year), age=int(age)), "when you turn", age, ".")
        return

# Here's our Main Program...
def age_calculator():
    exit_key = "x"
    exit_press = " "
    # Loop our program using While loop...
    while exit_key != exit_press:
        design()
        print("Follow this order: MM / DD / YY")
        print("Example: October 20 2000")
        print("Enter birthday: ")
        birth_month, birth_date, birth_year = [input("=> ") for i in range(3)]  # prompts the user for birthday.
        print("Enter today's date: ")
        recent_month, recent_date, recent_year = [input("=> ") for i in range(3)]  # prompts the user for today's date.

        birth_month = birth_month.capitalize()
        recent_month = recent_month.capitalize()

        # Check if our birth date and recent date is in range of calendars date.
        if int(birth_date) > 31:
            print("Invalid Birth date")
            exit()
        elif int(recent_date) > 31:
            print("Invalid Today's date")
            exit()

        # Formula to get the total age...
        total_age = (int(recent_year) - int(birth_year)) - 1
        # Check if we're going to update the age...
        if month_of_birth(birth_month=birth_month) <= todays_month(recent_month=recent_month) \
                and int(birth_date) <= int(recent_date):
            total_age += 1

        print()
        print("Processing...")
        time.sleep(3)
        print()
        print("Your Birthday is", birth_month, birth_date + ",", birth_year)
        print("The Date today is", recent_month, recent_date + ",", recent_year)
        print("Your age is", total_age, ".")
        print(dayOfYear(year=int(birth_year), month=month_of_birth(birth_month=birth_month), day=int(birth_date)))
        print(prediction())
        print()
        do_you(birth_year= int(birth_year))
        exit_press = input("Type 'x' to exit or any key to try again.\n=> ")
        exit_press = exit_press.lower()

age_calculator()