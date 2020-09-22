import compound
from math import pow
# To Calculate a compound interest
print("""   ______                                                   __   ____        __                           __
  / ____/____   ____ ___   ____   ____   __  __ ____   ____/ /  /  _/____   / /_ ___   _____ ___   _____ / /_
 / /    / __ \ / __ `__ \ / __ \ / __ \ / / / // __ \ / __  /   / / / __ \ / __// _ \ / ___// _ \ / ___// __/
/ /___ / /_/ // / / / / // /_/ // /_/ // /_/ // / / // /_/ /  _/ / / / / // /_ /  __// /   /  __/(__  )/ /_
\____/ \____//_/ /_/ /_// .___/ \____/ \__,_//_/ /_/ \__,_/  /___//_/ /_/ \__/ \___//_/    \___//____/ \__/
                       /_/                                                                                """)

print("""
        COMPOUND PERIOD
    Annually            1
    Semi-annually       2
    Quarterly           4
    Bi-monthly          6
    Monthly            12
    Semi-monthly       24
    Weekly             52
    Daily             365
    Continuously    infinity \n""")
def future_worth(principle_,rate_interest,number_period,compound_period):
    rate_interest /= 100
    future_func = principle_ * (1 + (rate_interest / compound_period)) ** (number_period * compound_period)
    return future_func
def principle(future_worth_,rate_interest,number_period,compound_period):
    rate_interest /= 100
    principle_func = future_worth_ * (1 + (rate_interest / compound_period)) ** (number_period * compound_period)
    return principle_func
def continuously(principle_,rate_interest,number_period,compound_period):
    rate_interest_number_period = (rate_interest / 100) * number_period
    future_con = principle_ * pow(compound_period, rate_interest_number_period)
    return future_con
## Ask what is missing?
response = input("What are you looking for? Future worth or Principle?: ")
response = response.lower()
if response == "future worth":
    Principle = int(input("What is the principle?: "))
    Rate_interest = float(input("What is the rate of interest?: "))
    Number_period = int(input("What is the number period?: "))
    period = input("what is the compound period?: ")
    period = period.lower()
    if period == "continuously":
        print("The Future Worth in continuously period is P", continuously(principle_= Principle, rate_interest= Rate_interest, number_period= Number_period, compound_period=compound.compound_period(period= period)))
    else:
        print("The Future worth is P", future_worth(principle_=Principle, rate_interest=Rate_interest, number_period=Number_period,
                       compound_period=compound.compound_period(period=period)))
elif response == "principle":
    Future_worth = int(input("What is the future worth?: "))
    Rate_interest = float(input("What is the rate of interest?: "))
    Number_period = int(input("What is the number period?: "))
    period = input("what is the compound period?: ")
    period = period.lower()
    print("The Principle is P", principle(future_worth_= Future_worth, rate_interest= Rate_interest, number_period= Number_period, compound_period=compound.compound_period(period= period)))