__author__ = "ResearchInMotion"

def multiply_2(number) :
    return number * 2

#here the mult_2 is an object and the multiply_2 is assigned to mult_2
mult_2 = multiply_2
print("3 * 2 = ",mult_2(3))

# passing the function in function
def do_math(func , number) :
    return func(number)

print("4 * 2 =",do_math(multiply_2 , 4))

# function return a function

def get_func_mutli_num(num):
    def multi_by(value):
        return value * num
    return multi_by

generated = get_func_mutli_num(5)
print(generated(9))