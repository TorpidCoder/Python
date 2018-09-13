selling = int(input("Please enter the selling price : "))

cost = int(input("Please enter the cost price : "))

if(selling>cost):
    profit = selling-cost
    print("The user has made a profit of {} ".format(profit))
else:
    profit = selling-cost
    print("The user has made loss of {} ".format(profit))
