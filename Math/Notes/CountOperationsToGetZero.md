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
In this optimized solution, we will be following the *Euclidian Algorithm*.  The reason being 
that when the we are working with a difference of the two numbers being very big, a lot of 
repetitive and identical subtraction operations will be perfomed (this give us some room for
optimization).  Basically what is happening here is while *num1* is greater than or 
equal to *num2* we subtract *num1* from *num2* until *num1* is less than *num2*.  At this 
point, *num1* represents *num1 mod num2*.  During this process, the number of operations that 
we will do is reprented by *floor(num1 / num2)*.  

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

> Optimizd Time Complexity: O(log max(num1, num2))

# Additional Resources

- https://www.youtube.com/watch?v=Jwf6ncRmhPg
- https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm


