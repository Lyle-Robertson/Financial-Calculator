import math


def investment_calculator():    # function containing input request and formulae for investment

    deposit_amount = float(input("\nHow much is your deposit?:\t\t"))   # request deposit amount
    interest_rate = float(input("At which interest?:\t\t\t\t"))   # request interest rate
    investment_length = int(input("How many years to you plan on investing for?:\t"))   # request investment period

    interest = input("Do you want simple or compound interest?(type simple/compound):\t")    # compound or simple

    if interest.lower() == "simple":    # if simple interest, determine interest earned with below equations

        # formula used  A = P(1 + r * t)
        # '%.2f' converts value into string with 2 decimal places

        investment_total = '%.2f' % (deposit_amount * (1 + ((interest_rate / 100) * investment_length)))
        interest_earned = '%.2f' % (float(investment_total) - deposit_amount)
        print(f"\nYour investment will grow to R {investment_total}, earning R {interest_earned} in interest")

    if interest.lower() == "compound":      # if compound interest, determine interest earned with below equations

        # formula used  A = P(1 + r) ^ t
        investment_total = '%.2f' % (deposit_amount * math.pow((1 + (interest_rate / 100)), investment_length))
        interest_earned = '%.2f' % (float(investment_total) - deposit_amount)
        print(f"\nYour investment will grow to R {investment_total}, earning R {interest_earned} in interest")

    if interest.lower() != "compound" and interest.lower() != "simple":
        # if anything other than simple or compound is entered

        print("Please enter only 'Simple or 'Compound'")    # display error message
        investment_calculator()     # rerun investment_calculator function


def bond_calculator():  # function contain input requests and calculations to determine repayable amount ond bond

    house_value = int(input("\nWhat is the value of the house currently:\t"))   # request current house value
    interest_rate = int(input("What is the interest rate?:\t\t\t\t\t"))   # request interest rate
    repay_time = int(input("In how many months will you complete the payment on the bond?:\t"))   # repayment period

    # formula used x = (i.P)/(1 - (1+i)^(-n))
    monthly_payment = '%.2f' % ((interest_rate / 100 * house_value) / (1 - math.pow((1 + interest_rate / 100), (0 - repay_time))))

    print(f"\nThe amount repayable per month is R {monthly_payment}")


def type_investment():  # function containing code to determine whether a bond or investment will be chosen

    # request input from use to determine whether an investment or bond
    investment_type = input("Chose either 'Investment' of 'Bond' from the menu below to continues (type "
                            "investment/bond):\n\n"
                            "investment\t\t-\tto calculate the amount of interest you'll earn on interest"
                            "\nbond\t\t\t-\tto calculate the amount you'll have have to pay on a home loan\n\n")

    if investment_type.lower() == "investment":  # .lower() use to make the input not case-sensitive
        investment_calculator()  # if investment selected, run the investment_calculator function

    if investment_type.lower() == "bond":
        bond_calculator()  # if bond is selected, run the bond_calculator function

    if investment_type.lower() != "investment" and investment_type.lower() != "bond":
        # if anything other than investment or bond is entered it will display the error message and rerun
        # the type_investment function

        print("Please Enter only 'Investment' or 'Bond'")
        type_investment()


type_investment()
