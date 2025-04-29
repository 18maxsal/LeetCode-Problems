# Problem Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # This Solution taken from LeetCode's writeup on the problem
        ans = 0
        max_element = max(nums)
        start = 0
        num_max = 0
        for i in range(len(nums)):
            if nums[i] == max_element:
                num_max += 1
            while num_max == k:
                if nums[start] == max_element:
                    num_max -= 1
                start += 1
            ans += start
        return ans



def test_one(test: Solution):
    nums = [1,3,2,3,3]
    k = 2
    print(f"Result from test_one: {test.countSubarrays(nums, k)}")


test = Solution()
test_one(test)