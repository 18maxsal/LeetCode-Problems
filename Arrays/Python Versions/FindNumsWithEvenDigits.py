# Problem Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                ans += 1
        return ans      


def test_one(test: Solution):
    nums = [12,345,2,6,7896]
    print(f"Result from test one: {test.findNumbers(nums)}")

def test_two(test: Solution):
    nums = [555,901,482,1771]
    print(f"Result from test two: {test.findNumbers(nums)}")

test = Solution()
test_one(test)
test_two(test)