list = ['p','q']

n = 4

data = ['{}{}'.format(x,y) for y in range(1,n+1) for x in list]
print(data)
