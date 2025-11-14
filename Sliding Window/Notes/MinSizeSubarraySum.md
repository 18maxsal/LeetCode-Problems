# Notes

> Problem Link: https://leetcode.com/problems/minimum-size-subarray-sum/

## Initial Intuition
This was an attempt at the sliding window algorithm but it was not properly
implemented which leads to a greater runtime than normal.  But the idea was 
to use the sliding window algorithm to find the smallest size sub-array where
it's sum is at least as big as the target.  My implentation works in principal, 
but has a poor runtime *O(N^2)*.  The reason why this is slow is becasue we 
iterate through the entire array with a fixed size window at a time.  This 
is what leads to the extremely poor runtime.

## Initial Code Solution

```Python
n = len(nums)

        for window_size in range(1, n + 1):
            curr_total = 0
            left, right = 0, 0
            curr_size = 0
            while right < n:
                
                if curr_size < window_size:
                    curr_total += nums[right]
                    right += 1
                    curr_size += 1

                    if curr_total >= target:
                        return window_size
                
                else:
                    curr_total -= nums[left]
                    curr_size -= 1
                    left += 1
        
        return 0
```
> Time Complexity: O(N^2)

# Optimized Intuition
This just follows the same intuition as above (i.e. we use the sliding window
algorithm here), except the code is optimized better.  The code is optimized 
such that right from the beginning, the size of the window increases where in
my original implementation, the size was fixed throughout the entire iteration
of the array.  This leads to a better runtime than what I originally implemented.

# Optimized Solution
```Python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0
```

> Optimizd Time Complexity: O(N)


