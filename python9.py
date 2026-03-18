#find the next largest number
#N=4,arr[]=[1,2,3,4]
#expected output: [3,4,4,-1]
#explanation: next largest number for 1 is 3, for 2 is 4, for 3 is 4 and for 4 there is no next largest number so -1
def nextLargest(arr):
    n = len(arr)
    result = []    
    for i in range(n):
        if i+2 < n:
            result.append(arr[i+2])
        else:
            result.append(-1)
    return result
arr = [1,3,2,4]
print(nextLargest(arr))