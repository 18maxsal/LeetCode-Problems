# Notes

> Problem Link: https://leetcode.com/problems/count-operations-to-obtain-zero/?envType=daily-question&envId=2025-11-09

## Initial Intuition
Not much of a explantation here other than just performing the operations as described in the problem statement.  Will
probably not be the most efficient way but is the most straight-forward since our constraints are somewhat reasonable.

## Initial Code Solution

```Python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            ans += 1

        return ans
```
> Time Complexity: O(min(num1, num2)) [NOTE: this time complexity was calculated by LeetCode Result page]

# Optimized Intuition
[Optimized Intuition for solving problem goes here]

# Optimized Solution
```Python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0  # total number of subtraction operations
        while num1 and num2:
            # each step of the Euclidean algorithm
            res += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return res
```

> Optimizd Time Complexity: ???


