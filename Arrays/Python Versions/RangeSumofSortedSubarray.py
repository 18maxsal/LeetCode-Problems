# Problem Link: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/?envType=daily-question&envId=2024-08-04

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        # 1. Get all subarrays
        sub_array = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub_array.append(sum(nums[i:j]))

        # 2. Sort result from [1] in non-decreasing order
        sub_array.sort()

        # 3 getting the sum of all numbers in between the index of left and right 
        # inclusive        
        ans = sum(sub_array[left - 1:right])
        mod = (10**9) + 7
        
        # 5. Return result and mod it by (10^9) + 7
        return ans  % mod

# Example Use
nums = [1,2,3,4]
n = 4
left = 1
right = 5
test = Solution()
result = test.rangeSum(nums = nums, n = n, left = left, right = right)
print(result)