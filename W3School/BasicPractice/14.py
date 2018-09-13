def withoutsign(a,b):
    while(b!=0):
        data = a & b
        a = a ^b
        b = data<<1
    return a


print(withoutsign(9,9))
