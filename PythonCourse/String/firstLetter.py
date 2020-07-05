__author__ = "ResearchInMotion"


# 1st type
message = input("Please enter the message  : ").upper().split()
solution = [word[0] for word in message]
print("".join(solution))

# 2nd type
for values in message:
    print(values[0].upper() , end="")

