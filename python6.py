#array rotation
# rotate the array to the right by number of steps given by the user
#n=1
#input: [1,2,3,4,5,6,7]
#output: [7,1,2,3,4,5,6]
def rotate_array(arr, n):
#    n = n % len(arr)  
 #   return arr[-n:] + arr[:-n]
    for i in range(n):
        last_element = arr[-1]  
        for j in range(len(arr) - 1, 0, -1):
            arr[j] = arr[j - 1]  
        arr[0] = last_element
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
n = 2
print(rotate_array(arr, n))