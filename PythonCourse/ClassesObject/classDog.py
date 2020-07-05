__author__ = "ResearchInMotion"

class Dog:

    def __init__(self , name , age , color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print("The dog named {} with color {} eats " .format(self.name , self.color))
    def bark(self):
        print("The dog named {} with color {} barks" .format(self.name , self.color))


dog = Dog(name="Gohan" , age = 23 , color="Green")
dog.eat()
dog.bark()

