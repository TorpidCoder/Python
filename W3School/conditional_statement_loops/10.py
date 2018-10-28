for vals in range(0,50):
    if(vals % 3 ==0):
        print("Fizz")
        if(vals % 5 ==0):
            print("Buzz")
            if(vals % 3 ==0) and (vals % 5 ==0):
                print("FizzBuzz")
