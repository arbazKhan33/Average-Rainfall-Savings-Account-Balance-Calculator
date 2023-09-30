# Arbaz Khan (1940280)

# Project 3
# Problem 1, Average Rainfall

yearsCalculated = 0;
monthlyRainfall = -1;
totalRain = 0;

yearsCalculated=int(input("How many years do you want to calculate rainfall for? "))
for i in range(0,yearsCalculated):
    print("Year",i+1,);
    for j in range(0,12):
            while (monthlyRainfall<0):
                print("Enter Monthly Raifall for month ",j+1);
                monthlyRainfall=int(input())
            totalRain+=monthlyRainfall;
            monthlyRainfall=-1;
            
print("You calculated Rainfall over",yearsCalculated*12, "months");
print("The total inches of Rainfall for",yearsCalculated*12, "
print("The average rainfall for this time period was ","{0:.2f}".format(totalRain/(yearsCalculated*12)),"inches");


# Problem 2, Savings Account Balance

totalDeposits = 0
totalWithdrawals = 0
totalInterests = 0

balance = float(input("Please enter your accounts starting balance: "))            
months = int(input("How many months has the account been open for? "))             
rate = float(input("Enter the annual interest rate on account: "))                  

for i in range(months):                            
    while(True):
        deposit = float(input("Enter deposit this month: "))
        if(deposit > 0):
            balance += deposit
            totalDeposits += deposit
            break
        print("Invalid entry, try again ")

    while(True):
        withdrawal = float(input('Enter the withdrawal in this month: '))
        if(withdrawal > 0):
            balance -= withdrawal
            totalWithdrawals += withdrawal
            break
        print("Invalid entry, try again ")

    interest = balance*(rate/12)          
    totalInterests = interest
    balance += interest

print("Your accounts ending balance is $" +str(round(balance,2)))
print("Total amount of deposits: $" +str(round(totalDeposits,2)))
print("Total amount of withdrawal: $" +str(round(totalWithdrawals,2)))
print("Total interest earned: $"+str(round(totalInterests,2)))