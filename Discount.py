## To calculate the Discount

print(""" ______   _____   ______     ______    ___   _____  _____  ____  _____  _________
|_   _ `.|_   _|.' ____ \  .' ___  | .'   `.|_   _||_   _||_   \|_   _||  _   _  |
  | | `. \ | |  | (___ \_|/ .'   \_|/  .-.  \ | |    | |    |   \ | |  |_/ | | \_|
  | |  | | | |   _.____`. | |       | |   | | | '    ' |    | |\ \| |      | |
 _| |_.' /_| |_ | \____) |\ `.___.' \  `-'  /  \ \__/ /    _| |_\   |_    _| |_
|______.'|_____| \______.' `.____ .' `.___.'    `.__.'    |_____|\____|  |_____|
                                                                                  """)
## Prompt for the principle
principle = float(input("Enter the principle: "))
## Prompt for the Future worth
future_worth = float(input("Enter the Future Worth: "))

## Calculate the Discount
discount = future_worth - principle
## Display the Discount
print("The Discount is P", discount)

## Calculate the Rate of discount
rate_discount = discount / future_worth
## Display the Rate of Discount
print("The Rate of discount is", rate_discount, "or", rate_discount * 100, "%")

## Calculate the interest
interest = rate_discount  / (1 - rate_discount)
## Display the interest
print("The interest is", interest, "or", interest * 100, "%")