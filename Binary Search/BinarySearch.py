# Link To Problem: https://leetcode.com/problems/binary-search/

def binarysearch(arr, low, high, target):
    
    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == target: # Found Target if true
            return mid
        
        elif arr[mid] < target: # arr[mid] is less than the target, ignoring the left half of the array
            low = mid + 1
        
        else: # arr[mid] is greater than the target, ignoring the right half of the array
            high = mid - 1
    
    return -1