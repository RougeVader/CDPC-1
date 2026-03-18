#product of array except self
#sample input: [1,2,3,4]
#expected output: [24,12,8,6]
#logic : uses 2 passes,one from left to right and another from right to left, to calculate the product of elements 

arr=[1,2,3,4]
n=len(arr)
output=[1]*n
for i in range(1,n):
    output[i]=output[i-1]*arr[i-1]
    
R=1
for i in range(n-1,-1,-1):
    output[i]=output[i]*R
    R=R*arr[i]
print(output)
