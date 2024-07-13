# Link to Problem: https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index = i
            else:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index = i + 1


        # num_zeros = 0
        # for i in nums:
        #     if i == 0:
        #         num_zeros += 1
        # first_zero_index = 0
        # first_zero = False
        # for i in range(len(nums)):
        #     if nums[i] == 0 and first_zero == False:
        #         first_zero_index = i
        #         first_zero = True
        #     else:
        #         nums[first_zero_index - 1] = nums[i] 
        # curr_zero_index = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         curr_zero_index = i
        #     elif nums[i] != 0:
        #         nums[curr_zero_index], nums[i] = nums[i], nums[curr_zero_index]
        #         curr_zero_index = i
nums = [0,1,0,3,12]
test = Solution()
print("Before: ", nums)
test.moveZeroes(nums)
print("After: ", nums)