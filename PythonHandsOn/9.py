original_number = int(input("Please enter a number : "))



while(True):

    guess_number = int(input("Please enter a number : "))

    if(original_number==guess_number):
        print("Hey you are so sharp")
    elif(original_number>guess_number):
        print("Your guess so low")
    elif(original_number<guess_number):
        print("Your guess so high")

    elif(guess_number ==0):
        sys.exit()
