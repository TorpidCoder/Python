netAmount = 0
while True:
        val = input("Enter the input :")
        if(val=='e'):
            break
        elif(val=='d'):
            money = int(input("enter the amount : "))
            netAmount+=money
        elif(val=='w'):
            money = int(input("enter the amount : "))
            netAmount-=money


print("The net amount is : " , netAmount)
