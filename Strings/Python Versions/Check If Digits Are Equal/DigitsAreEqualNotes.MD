# Notes

> Problem Link: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/?envType=daily-question&envId=2025-10-23

## Initial Intuition
The basic idea here is to just simply follow the operations as stated in the problem by just iterating through the string while the string has a length greater than 2 and update the string at the end of each iteration of iterating through the string.

## Initial Code Solution

```Python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = ""

            for i in range(1, len(s)):
                new_s += str((int(s[i]) + int(s[i - 1])) % 10)
            s = new_s
            # print(s)
        if len(s) != 2:
            return False


        return s[0] == s[1]
```
> Time Complexity: ???
