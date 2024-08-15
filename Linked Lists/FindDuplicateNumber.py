# Link to problem: https://leetcode.com/problems/find-the-duplicate-number/description/
# Makes use of Floyd's Cycle Detection Algo, albeit slightly modified for purposes of the problem
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True: # Finding the first point of intersection
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True: # Finding the actual duplicate number
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

nums = [1,3,4,2,2]
test = Solution()
result = test.findDuplicate(nums = nums)
print(result)