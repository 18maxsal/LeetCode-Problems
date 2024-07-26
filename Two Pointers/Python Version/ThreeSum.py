# Problem Link: https://leetcode.com/problems/3sum/description/

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        start = 0
        end = len(nums) - 1
        curr_target = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)): # At this point it is essentially TwoSumII
            pass
    
    def twoSumII(self, nums:List[int], toSkip: int, target: int):
        left = 0
        right = len(nums) - 1
        while left < right:
            if left != toSkip and right != toSkip:
                if nums[left] + nums[right] == target:
                    return [left, right]
                
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1