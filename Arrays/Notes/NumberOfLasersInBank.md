# Notes

> Problem Link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/?envType=daily-question&envId=2025-10-27

## Initial Intuition
[Initial Intuition for solving problem goes here]

## Initial Code Solution

```Python
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        devices_row = []
        for row in bank:
            curr_devices = 0
            for i in row:
                if i == "1":
                    curr_devices += 1
            if curr_devices > 0:
                devices_row.append(curr_devices)
        
        for i in range(1, len(devices_row)):
            ans += devices_row[i - 1] * devices_row[i]
        
        return ans
```
> Time Complexity: ???
