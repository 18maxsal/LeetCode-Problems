# Notes

> Problem Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/submissions/1829117479/

## Initial Intuition
Not really much of an initial intuition here.  Solution is taken from LC's write up as I was unable to 
solve the question reasonably.

## Initial Code Solution

```Python
pass
```
> Time Complexity: ???

# Optimized Intuition
[Optimized Intuition for solving problem goes here]

# Optimized Solution
```Python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = 0
        current_total = 0
        left, right = 0, 0
        num_to_index = {}
        window_size = right - left

        while right < n:
            curr_num = nums[right]
            last_occurrence = num_to_index.get(curr_num, -1)

            while left <= last_occurrence or window_size + 1 > k:
                current_total -= nums[left]
                left += 1
                window_size = right - left
            num_to_index[curr_num] = right
            current_total += nums[right]
            if window_size + 1 == k:
                ans = max(ans, current_total)
            right += 1
            window_size = right - left
        return ans
```

> Optimizd Time Complexity: ???


