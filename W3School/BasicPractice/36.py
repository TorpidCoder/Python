def add_numbers(a,b):
    if not(isinstance(a,int) and isinstance(b,int)):
        raise TypeError("Not of same data type")
    return a+b



print(add_numbers(10,20))
