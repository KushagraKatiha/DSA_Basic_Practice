## Binary Search 

## Function Defination
def binarySearch(arr, x, lb, hb):
 while lb<=hb:
    if len(arr) == 0:
        if arr[0] == x:
            return arr
        else: 
            return -1
    else:
        mid = lb + (hb-lb)//2

        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
           return binarySearch(arr, x, lb, mid-1)
        else:
            return binarySearch(arr, x, mid+1, hb)
    

## Driver Code
arr = [1,5,6,2,8,9,100,50,20,46,78]
x = 20
lb = 0
hb = len(arr)-1
result = binarySearch(arr, x, lb, hb)
print(result)