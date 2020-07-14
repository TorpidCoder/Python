__author__ = "ResearchInMotion"

# def takeList(limit):
#     arr = []
#     for vals in range(limit):
#         arr.append(int(input("Enter the number : ")))
#     return arr

arr = range(1,10)

def odd(num):
    if num %2 == 0:
        return False
    else:
        return True

def changeList(list , func):
    odd_vals = []
    for i in list:
        if func(i):
            odd_vals.append(i)
    return odd_vals

print(changeList(arr ,odd ))
