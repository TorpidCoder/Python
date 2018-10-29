def cases(str):

    upper = 0
    lower = 0

    for vals in str:
        if(vals.isupper()):
            upper+=1
        elif(vals.islower()):
            lower+=1


    return upper,lower



print(cases("The quick Brow Fox"))
