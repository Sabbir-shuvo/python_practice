x=int(input("Please enter a year "))
if((x%4==0 and x%100!=0) or x%400==0):
    print(str(x)+" is a leap year")
else:
    print((str(x)+" is not a leap year"))