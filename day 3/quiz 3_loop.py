#Write a python program that will take last term of the series ‘n’ and show the sum of this series:
#1-2+3-4+5……..n=?

x=int(input("please enter a number"))
evensum=0
oddsum=0
for number in range(1,x+1):
    if(number%2!=0):
        oddsum=oddsum+number
    else:
        evensum=evensum+number
sum=(oddsum-evensum)

print(sum)



