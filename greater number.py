x=int(input("number1="))
y=int(input("number2="))
z=int(input("number3="))

if(x>y and x>z):
    print(str(x)+"is maximum")
elif(y>x and y>z):
    print( str(y) +"is maximum")
else:
    print(str(z)+" is maximum")


