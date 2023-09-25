## Linear Search Program 

## Function Defination
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1


## Driver Code

arr = [1,5,6,2,8,9]
x = 6
result = linearSearch(arr, x)
print(result)