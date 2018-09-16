value = input("enter the input : ")
sum = 0
while True:
    if(value=='e'):
        break
    elif(value=='m'):
        move = input("Enter the direction : ")
        if(move =='Up'):
            val_up = int(input("Enter the value of up : "))
            sum+=val_up
        elif(move =='Down'):
            val_up = int(input("Enter the value of down : "))
            sum-=val_up
        elif(move =='Left'):
            val_up = int(input("Enter the value of left : "))
            sum-=val_up
        elif(move =='Right'):
            val_up = int(input("Enter the value of right : "))
            sum+=val_up
        else:
            break

print("The movemnt done is : " , sum)
