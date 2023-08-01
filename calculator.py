# how does this shit with input work broo

user_input = int(input("Type 1 for wage, type sth else for mwst"))



if user_input == 1:

    # var for difining

    wage = int(input("wage per hour"))
    time_day = int(input("daily working time in hours"))
    month_days = input("monthly workdays")
    tax = float(input("how many taxes (float integer, for example 0.35)"))
    tax2 = float(int(1) - float(tax))
    currency = str(input("please type your currency"))

    # var for calculating

    monthly_income_pre_tax = int(wage) * int(time_day) * int(month_days)
    monthly_income_after_tax = int(wage) * int(time_day) * int(month_days) * float(tax2)
    yearly_income_pre_tax = monthly_income_pre_tax * 12 
    yearly_income_after_tax = monthly_income_after_tax * 12
    wage_after_tax = wage * tax2

    # code for showing results

    print("Your monthly pre tax income is: " + str(monthly_income_pre_tax) + currency)
    print("Your monthly income after paying taxes is " + str(monthly_income_after_tax) + currency)
    print("Your yearly income pre tax is  " + str(yearly_income_pre_tax) + currency)
    print("Your yearly income after paying Taxes is " + str(yearly_income_after_tax) + currency)
 
elif user_input !=1:
    # code for defining MEHRWERTSTEUER

    price_pre_tax = float(input("please put the price of the product here"))
    mwsttax = float(input("please put the Mehrwertsteuer here (in Germany we say Mehrwertsteuer)"))
    mwsttax2 = int(1) - float(mwsttax)
    price_after_tax = int(price_pre_tax) * float(mwsttax2)
    currency = str(input("Please type your currency"))

    # code for showing price after tax

    print("Your product costs " + str(price_after_tax) + currency)


# code that the program doesnt cancel emidiantly 

input("push a button on your keyboard")

