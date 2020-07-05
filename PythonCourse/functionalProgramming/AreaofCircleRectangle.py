__author__ = "ResearchInMotion"

import math

def getArea(shape):
    if(shape=='circle'):
        areaCirce()
    elif(shape=='rectangle'):
        areaRectangle()
    else:
        print("The shape is not present in the list")

def areaCirce():
    radius = int(input("Please enter the radius : "))
    area = math.pi * math.pow(radius,2)
    print("The area of circle is " , area)
def areaRectangle():
    length = int(input("Please enter the length : "))
    breadth = int(input("Please enter the breadth : "))
    area = length * breadth
    print("The area of rectangle is " , area)


def main():
    shape = input("Please enter the shape : ")
    getArea(shape)
main()