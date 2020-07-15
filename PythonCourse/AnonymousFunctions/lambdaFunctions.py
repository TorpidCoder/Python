__author__ = "ResearchInMotion"
import random

sum = lambda a , b: a+b
print("The sum is : " , sum(4,5))

can_vote = lambda age : True if age >=18 else False
print("Can Vote : " , can_vote(23))

list_sqaure = [lambda x : x**2,
               lambda x : x**3,
               lambda x : x**4]

for func in list_sqaure:
    print(func(5))

flip_list = []
for i in range(1,101):
    flip_list += random.choice(['H' , 'T'])
print("Heads : " , flip_list.count('H'))
print("Tails : " , flip_list.count('T'))