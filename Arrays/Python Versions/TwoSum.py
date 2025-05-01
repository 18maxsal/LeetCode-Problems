# Problem Link: https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # This solution works, but not optimal --> O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # The most optimal solution, uses a hashmap --> O(n)
        indexes = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indexes:
                return [indexes[difference], i]
            indexes[nums[i]] = i

def test_one(test: Solution):
    nums = [2,7,11,15]
    target = 9
    print(f"Result from test one: {test.twoSum(nums, target)}")

def test_two(test: Solution):
    nums = [3,2,4]
    target = 6
    print(f"Result from test two: {test.twoSum(nums, target)}")

def test_three(test: Solution):
    nums = [3,3]
    target = 6
    print(f"Result from test three: {test.twoSum(nums, target)}")

def main():
    test = Solution()
    test_one(test)
    test_two(test)
    test_three(test)

if __name__ == "__main__":
    main()