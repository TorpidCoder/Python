__author__ = "ResearchInMotion"

sentence = "Let's take LeetCode contest"
sentence = (sentence.split(" "))
newsentence = []
for values in sentence:
    rev = values[::-1]
    newsentence.append(rev)

print(" ".join(newsentence))



