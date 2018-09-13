salary = int(input("Please enter the salary : "))


if((salary>5000) & (salary<10000)):

    hra = salary*0.10
    da =salary*0.5


elif((salary>10001) & (salary<15000)):
    hra = salary*0.15
    da =salary*0.8

print("The hra is : ",hra)
print("The da is : ",da)
