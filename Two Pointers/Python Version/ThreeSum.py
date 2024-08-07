# Problem Link: https://leetcode.com/problems/3sum/description/

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right: # From this point is essentially TwoPointerII
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left - 1] and left < right: # How to deal with repeating numbers
                        left += 1
        return ans

nums = [-1,0,1,2,-1,-4]
test = Solution()
result = test.threeSum(nums)
print("Result: ", result)