fac=1
x=int(input("insert a number"))
if(x>=0):
    for number in range (1,x+1):
        fac=fac*number
    print(fac)
else:
    print("insert a positive number")

