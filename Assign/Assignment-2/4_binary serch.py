def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1

myArray = input("Enter Enter number in search:")
myTarget = input("Enter value to find(as per above array):")
my=myTarget
result = binarySearch(myArray, my)
if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")