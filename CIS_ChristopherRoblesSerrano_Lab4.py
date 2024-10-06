# Module 5 Lab-5
# Christopher Robles Serrano
# 10/5/24
# This programs calculates bonuses for the store and the employees based on the monthly sales and sales increase respectively.
# The program takes users inputs to find the monthly sales, the sales percentage increase, calculate the store bonus, calculate employee bonus, and prints the store/employee bonuses.

# The main function
def main():
    
    #Initialzing local variables
    monthlySales = getSales("Enter the monthly sales $")
    salesIncrease = getIncrease("Enter the sales increase:")
    storeAmount = calcStoreBonus(monthlySales)
    empAmount = calcEmpBonus(salesIncrease)
    
    #Printing our information to the terminal
    printBonus(storeAmount,empAmount)

#Function to find monthly sales    
def getSales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales

#Function to find the sales increase
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100
    return salesIncrease

#Function to calculate the store bonus based of the monthly sales    
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

#Function to calculate the employee bonus based on the sales increase        
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else: 
        empAmount = 0
    return empAmount

#Function to print the store bonus and employee bonus to the terminal         
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $:", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible!")

#Calling the main function
main()
