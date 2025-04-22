# Problem Link: https://leetcode.com/problems/count-the-hidden-sequences/description/?envType=daily-question&envId=2025-04-21

from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = 0
        y = 0
        cur = 0
        for i in differences:
            cur += i
            x = min(x, cur)
            y = max(y, cur)
            if y - x > upper - lower:
                return 0
        return (upper - lower) - (y - x) + 1


def test_one(test: Solution):
    differences = [1, -3, 4]
    lower = 1
    upper = 6
    return test.numberOfArrays(differences, lower, upper)




test = Solution()
print(f"Result from test one: {test_one}")