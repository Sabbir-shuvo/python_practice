x=int(input("Please insert the number"))
if(x>=90 and x<=100):
    print("A")
elif(x>=80 and x<=89):
    print("B")
elif(x>=60 and x<=79):
    print("C")
elif(x<60 and x>0):
    print("F")
else:
    print("Please enter a number between 0-100")