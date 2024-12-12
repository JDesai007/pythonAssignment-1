def binarySearch(arr, targetVal):
    left ,right= 0,len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1

myArray = list(map(int, input("Enter a sorted array (space-separated): ").split()))
myTarget =int(input("Enter the target element: "))
result = binarySearch(myArray, myTarget)
if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")