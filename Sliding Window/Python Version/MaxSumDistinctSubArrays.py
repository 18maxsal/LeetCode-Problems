from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = 0
        current_total = 0
        left, right = 0, 0
        num_to_index = {}
        window_size = right - left

        while right < n:
            curr_num = nums[right]
            last_occurrence = num_to_index.get(curr_num, -1)

            while left <= last_occurrence or window_size + 1 > k:
                current_total -= nums[left]
                left += 1
                window_size = right - left
            num_to_index[curr_num] = right
            current_total += nums[right]
            if window_size + 1 == k:
                ans = max(ans, current_total)
            right += 1
            window_size = right - left
        return ans






def testOne(test: Solution):
    nums = [1,5,4,2,9,9,9]
    k = 3
    result = test.maximumSubarraySum(nums, k)
    print(result)

def testTwo(test: Solution):
    nums = [4, 4, 4]
    k = 3
    result = test.maximumSubarraySum(nums, k)
    print(result)



def main():
    test = Solution()
    testOne(test)
    testTwo(test)

if __name__ == "__main__":
    main()