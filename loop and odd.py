odd_sum=0
even_sum=0
for number in range(1,1000):
    if(number%2!=0):
        odd_sum=odd_sum+number
    else:
        even_sum=even_sum+number
print(str(odd_sum)+"is odd sum")
print(str(even_sum)+ "is even sum")
