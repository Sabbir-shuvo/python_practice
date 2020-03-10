result=0
for number in range(1,101):
    result=result+(number**number)
print(result)


oddresult=0
evenresult=0
for number in range(1,11):
    if(number%2!=0):
        oddresult=oddresult+(number**number)
    else:
        evenresult=evenresult+(number**number)
print(oddresult)
print(evenresult)