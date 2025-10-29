# Notes

> Problem Link: https://leetcode.com/problems/smallest-number-with-all-set-bits/?envType=daily-question&envId=2025-10-29

## Initial Intuition
The idea here is fairly straightforward.  Here, we just convert the given number 
into its binary representation (i.e. 1 -> 1, 2 -> 01, 3 -> 11, etc.) and treat it as an 
array.  Once we have this array, we just switch any "0"'s we see and convert them 
into "1"'s.  This works because we are looking for a number that is at least n.
After that, we convert the number we found and convert it back into an integer.
Note that this solution is made simpler since it is written in Python and may 
not be as viable in other programming languages; I am just leveraging what I 
have available to me since I am using Python.

## Initial Code Solution

```Python
class Solution:
    def smallestNumber(self, n: int) -> int:
        n = list(bin(n))
        n = n[2:]
        has_zero = False
        for i in range(len(n)):
            if n[i] == '0':
                has_zero = True
                n[i] = '1'
        return int("".join(n), 2)
```
> Time Complexity: O(n)??? [NOTE: LC says it's O(log(n))]

# Optimized Intuition
[Optimized Intuition for solving problem goes here]

# Optimized Solution
```Python
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x
```

> Optimizd Time Complexity: O(log(n))


