# Notes

> Problem Link: https://leetcode.com/problems/make-array-elements-equal-to-zero/?envType=daily-question&envId=2025-10-28

## Initial Intuition
A slightly mathy intuition with some insiration from prefix sum algorithms.  Here, we iterate
through the array of numbers while getting a running sum of non-zero numbers seen so far.
Once we have run into a zero in the array, we get the total sum of the remaining numbers in the 
array and compare to our running sum so far.  If the running sum and sum of what we have not 
seen are the same then we increment by two (since we can make the whole array become zero
no matter which direction we start with); and if the difference is by one, then we will 
increment our answer by one since the simulation will only be successful in one of the 
two directions.  After that, we just return our recorded answer.

## Initial Code Solution

```Python
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] != 0:
                total += nums[i]
            
            else:
                other_side = 0
                for j in range(i, n):
                    if nums[j] != 0:
                        other_side += nums[j]
                if total == other_side:
                    ans += 2
                elif total == (other_side + 1):
                    ans += 1
                elif (total + 1) == other_side:
                    ans += 1
        return ans
```
>  Initial Time Complexity: O(n<sup>2</sup>)

# Optimized Intuition
The idea here is much of the same except we optimize for the prefix sum algorithm above.

# Optimized Solution

```Python
class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0
        s = sum(nums)
        left, right = 0, s
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
        return ans
```

> Optimized Time Complexity: O(n)