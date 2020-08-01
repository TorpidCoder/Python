__author__ = "ResearchInMotion"


sentence = input("Enter the word : ")
for words in ("!?',;.") :
    sentence.replace(words , " ")
word = sentence.split()
print((sum(len(values) for values in word)/len(word)))

