Sales = int(input("Please enter the number : "))

if(Sales>1) & (Sales<10000):
    commission = 0.4*Sales

elif(Sales>10001) & (Sales<20000):
    commission = 0.5*Sales

elif(Sales>20001) & (Sales<30000):
    commission = 0.6*Sales

elif(Sales>31000):
    commission = 0.7*Sales

print("The commission is :{} ".format(commission))
