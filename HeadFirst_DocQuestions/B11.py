salary = int(input("Please enter the salary : "))

if(salary>9000):
    income_tax = salary*0.40
elif(salary>7500) & (salary<8999):
    income_tax = salary*0.30
elif(salary<7500):
    income_tax= salary*0.20

print("The income tax is {}".format(income_tax))
