word_1 = input("enter word 1 : ")
word_2 = input("enter word 2 : ")


word3 = word_1.replace(word_1[0] , word_2[0])
word4 = word_2.replace(word_2[0],word_1[0])
print(word3)
print(word4)
