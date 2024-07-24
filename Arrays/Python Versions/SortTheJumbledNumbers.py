# Problem Link: https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24
from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new_nums = {}

        for i in nums: # Converting to the mapped numbers system
            new_nums[self.jumbledNumber(mapping, str(i))] = i


        # Sort the mapped numbers b using quicksort
        keys_sorted = list(new_nums.keys())
        low = 0
        high = len(keys_sorted) - 1
        self.quickSort(keys_sorted, low, high)
        print("keys_sorted: ", keys_sorted)
        # for i in new_nums.keys():
        #     pass

        return new_nums
    
    def partition(self, new_nums, low, high):

        pivot = new_nums[high]

        i = low - 1

        for j in range(low, high):
            if new_nums[j] <= pivot:
                i = i + 1
                new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
        new_nums[i + 1], new_nums[high] = new_nums[high], new_nums[i + 1]

        return i + 1
    
    def quickSort(self, new_nums, low, high):
        if low < high:
            pi = self.partition(new_nums, low, high)
            self.quickSort(new_nums, low, pi - 1)
            self.quickSort(new_nums, pi + 1, high)

        


    def jumbledNumber(self, mapping: List[int], num: str):
        result = ""
        for i in num:
            result += str(mapping[int(i)])
        return result

mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
test = Solution()
result = test.sortJumbled(mapping, nums)

print("Result: ", result)