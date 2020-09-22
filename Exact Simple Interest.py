# To solve for the Exact Simple Interest
# Interest = Pin

print("""     _______  __ ___   ____________   _____ ______  _______  __    ______   _____   __________________  _________________
   / ____/ |/ //   | / ____/_  __/  / ___//  _/  |/  / __ \/ /   / ____/  /  _/ | / /_  __/ ____/ __ \/ ____/ ___/_  __/
  / __/  |   // /| |/ /     / /     \__ \ / // /|_/ / /_/ / /   / __/     / //  |/ / / / / __/ / /_/ / __/  \__ \ / /
 / /___ /   |/ ___ / /___  / /     ___/ // // /  / / ____/ /___/ /___   _/ // /|  / / / / /___/ _, _/ /___ ___/ // /
/_____//_/|_/_/  |_\____/ /_/     /____/___/_/  /_/_/   /_____/_____/  /___/_/ |_/ /_/ /_____/_/ |_/_____//____//_/
                                                                                                                        """)
# Prompt the user to enter the Principle
principle = float(input("Enter the Principle: "))
# Prompt the user to enter the Rate of interest
Rate_interest = float(input("Enter the Rate of interest(decimal): "))
# Prompt the user to enter the number of interest period
n = int(input("Enter days: "))
# Calculate the Interest
interest_leap = principle * (n / 366) * Rate_interest
interest_normal = principle * (n / 365) * Rate_interest

# Display the Interest
print("The interest in leap year is P", interest_leap)
print("The interest in normal year is P", interest_normal)