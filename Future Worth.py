# To Calculate Future Worth
# F = P (1 + in)

print("""     ________  __________  ______  ______   _       ______  ____  ________  __
   / ____/ / / /_  __/ / / / __ \/ ____/  | |     / / __ \/ __ \/_  __/ / / /
  / /_  / / / / / / / / / / /_/ / __/     | | /| / / / / / /_/ / / / / /_/ /
 / __/ / /_/ / / / / /_/ / _, _/ /___     | |/ |/ / /_/ / _, _/ / / / __  /
/_/    \____/ /_/  \____/_/ |_/_____/     |__/|__/\____/_/ |_| /_/ /_/ /_/
                                                                            """)
# Prompt the user to enter the Principle
principle = float(input("Enter the Principle: "))
# Prompt the user to enter the Rate of interest
Rate_interest = float(input("Enter the Rate of interest(decimal): "))
# Prompt the user to enter the number of interest period
n = int(input("Enter months: "))
# Calculate the Future Worth
Future_worth = principle * (1 + (Rate_interest * (n / 12)))
# Display Future Worth
print("The Future worth is P", Future_worth)
