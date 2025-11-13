# Problem Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24
from typing import List

class Solution:
    
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_distinct = set(nums)
        ans = 0
        left = 0
        right = 0
        while left < len(nums):
            to_check = set(nums[left:(right + 1)]) 
            if len(to_check) == len(num_distinct):
                ans += 1
            elif len(to_check) > len(num_distinct):
                left += 1
                right = left
                continue
            right += 1
            if right == len(nums):
                left += 1
                right = left

        return ans
    
        # Solution below is from the LeetCode Writeup:
        # res = 0
        # cnt = {}
        # n = len(nums)
        # right = 0
        # distinct = len(set(nums))
        # for left in range(n):
        #     if left > 0:
        #         remove = nums[left - 1]
        #         cnt[remove] -= 1
        #         if cnt[remove] == 0:
        #             cnt.pop(remove)
        #     while right < n and len(cnt) < distinct:
        #         add = nums[right]
        #         cnt[add] = cnt.get(add, 0) + 1
        #         right += 1
        #     if len(cnt) == distinct:
        #         res += n - right + 1
        # return res
    

def test_one(test: Solution):
    nums = [1,3,1,2,2]
    print(f"Result from test One: {test.countCompleteSubarrays(nums)}")


test = Solution()
test_one(test)