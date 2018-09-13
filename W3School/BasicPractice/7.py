from collections import Counter

with open("/Users/sahilnagpal/Desktop/Python/W3School/File.txt") as file:
    print(Counter(file.read().split(" ")))
