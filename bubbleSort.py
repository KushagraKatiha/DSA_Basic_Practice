## Bubble Sort

## Function defination
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr



## Driver Code
arr = [1,5,6,2,8,9]

result = bubbleSort(arr)
print(result)