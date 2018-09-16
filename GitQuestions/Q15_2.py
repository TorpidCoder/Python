number = int(input("Enter the number  :  "))

n1 = int('%s'%number)
n2 = int('%s%s'%(number,number))
n3 = int('%s%s%s'%(number,number,number))
n4 = int('%s%s%s%s'%(number,number,number,number))


print(n1+n2+n3+n4)
