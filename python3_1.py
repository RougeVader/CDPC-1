n=int(input("enter a number:"))
x=int(input("enter a number:"))
sum1=0
for i in range(1,n):
    sum1=sum1+(x**i)/i
print("the sum is:",sum1)
