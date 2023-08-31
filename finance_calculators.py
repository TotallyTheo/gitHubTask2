import math
print("Investment -to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
#The user must select what calculation they want to do and enter the value of money they want to envest or bond value
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()

if user_choice == "investment":
    print("You chose the investment option")
    
    #now the investment math will follow
    investemnt_ammount = int(input("What is the amount of money that you will be depositing?\n"))
    interest_rate = int(input("Please enter the interest rate number\n"))
    years_investing = int(input("For how long will you be investing?\n"))
    interest = input("Do you want the simple or compound interest?\n").lower()
    
    #second if-statement to do the math of the compound or simple investment option
    if interest == "compound":
        total_value = investemnt_ammount * math.pow((1+interest_rate),years_investing) #I cant get my compound interest calculation to work and dont know what I am doing wrong
        print(f"R{total_value}")
    elif interest == "simple":
        total_value = investemnt_ammount *(1 + interest_rate * years_investing)
        print(f"R{total_value}")
    else:
        print("error, did not select one of the options")

#Now follows if the user chose the bond function    
elif user_choice == "bond":
    print("You chose the bond option")
    bond_ammount = int(input("What is the value of the house?\n"))
    bond_rate = int(input("What is the interest rate?\n"))
    bond_montly_repay = int(input("How many months is it going to take to repay the bond?\n"))
    #the math to do the bond calculation
    bond_repayment = (bond_rate * bond_ammount)/(1 - (1+ bond_rate)**(-bond_montly_repay))
    print(f"Your monthly repayment will be R{bond_repayment}")

else:
    print("error, you did not select a valid option")
