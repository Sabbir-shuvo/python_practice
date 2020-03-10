gene="ATCCCCGGGTTTATATACCGGAT"

#total_A= gene.count("T")
#print(total_A)

totalA=totalC=totalT=totalG=0

for i in gene:
    if(i=="A"):
        totalA=totalA+1
    elif(i=="C"):
        totalC=totalC+1
    elif (i == "T"):
        totalT = totalT + 1
    elif (i == "G"):
        totalG = totalG + 1
    else:
        print("wrong")
print(" total 'A'"+str(totalA) +"\n total T "+str(totalT) + "\n total C "+str(totalC)+"\n total G "+str(totalG))


