try:
    file = open('sahil.txt' ,'a')
    file.write("is my new check \n")
except IOError as e:
    print("The error is : " , e)
else:
    print("the file write successfully")
    file.close()
