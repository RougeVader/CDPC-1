#find the majority element in an array[an element that appears more than n/2 times]
#sample input: [2,2,1,1,1,2,2]  
#expected output: 2

count=0
arr=[123,12,3,4,5,6,7,8,11,11,23,12,1234,123,11,11,11,11,11,11,11,11,11,11,11]
for i in arr:
    if count == 0:
        majority = i
    count += 1 if i == majority else -1

if arr.count(majority) > len(arr) // 2:
    print(majority)
else:
    print("No majority element found")