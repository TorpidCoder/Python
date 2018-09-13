def area(principle,rate,time):
    return principle*rate*time/100


principle = int(input("principle is : "))
rate = int(input("rate is : "))
time = int(input("time is : "))

print(area(principle,rate,time))
