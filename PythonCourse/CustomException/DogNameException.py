__author__ = "ResearchInMotion"

class DogException(Exception):
    def __init__(self , *args , **kwargs):
        Exception.__init__(self,*args , **kwargs)

    try:
        dogname = input("Please enter the dog name : ")
        if (any(char.isdigit() for char in dogname)):
            raise Exception
    except Exception:
        print("The dog name does not contain the numbers")