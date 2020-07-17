__author__ = "ResearchInMotion"

listly = ([1,2,3],
          [4,5,6],
          [7,8,9])

firstcol = [col[1] for col in listly]
secondcol = [col[2] for col in listly]
print(firstcol)
print(secondcol)

allcross = [listly[m][m] for m in range(len(listly))]
print(allcross)