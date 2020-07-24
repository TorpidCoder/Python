__author__ = "ResearchInMotion"

from random import choice
from string import ascii_lowercase
n= int(input("Number :  "))
if(n%2==0):
    stringvals = "".join("a"*(n-1) + "b"*1)
else:
    stringvals = "".join("a" * n)
print(stringvals)