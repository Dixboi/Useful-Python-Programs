# To solve for the Ordinary Simple Interest
# Interest = Pin

print("""    ____  ____  ____  _____   _____    ______  __   _____ ______  _______  __    ______   _____   __________________  _________________
  / __ \/ __ \/ __ \/  _/ | / /   |  / __ \ \/ /  / ___//  _/  |/  / __ \/ /   / ____/  /  _/ | / /_  __/ ____/ __ \/ ____/ ___/_  __/
 / / / / /_/ / / / // //  |/ / /| | / /_/ /\  /   \__ \ / // /|_/ / /_/ / /   / __/     / //  |/ / / / / __/ / /_/ / __/  \__ \ / /
/ /_/ / _, _/ /_/ // // /|  / ___ |/ _, _/ / /   ___/ // // /  / / ____/ /___/ /___   _/ // /|  / / / / /___/ _, _/ /___ ___/ // /
\____/_/ |_/_____/___/_/ |_/_/  |_/_/ |_| /_/   /____/___/_/  /_/_/   /_____/_____/  /___/_/ |_/ /_/ /_____/_/ |_/_____//____//_/
                                                                                                                                     """)
# Prompt the user to enter the Principle
principle = float(input("Enter the Principle: "))
# Prompt the user to enter the Rate of interest
Rate_interest = float(input("Enter the Rate of interest(decimal): "))
# Prompt the user to enter the number of interest period
months = int(input("Enter months: "))
days = int(input("Enter days: "))
# Convert the months to ordinary days
def ordinary_days(Months, Days):
    n = (Months * 30) + Days
    return n

# Calculate the Interest
interest = principle * (ordinary_days(Months=months, Days=days) / 360) * Rate_interest

# Display the Interest
print("The interest is P", interest)
