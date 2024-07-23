# Problem Link: https://leetcode.com/problems/sort-array-by-increasing-frequency/description/?envType=daily-question&envId=2024-07-23

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        dictionary = {} # A dictionary that will contain all of the frequencies in the array 
        ans = []

        for i in nums: # Getting counts and putting them into the dicitonary
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        return sorted(nums, key = lambda x: (dictionary[x], -x)) # Not Sure about this line yet, but it does make use of Dictionary comprehension
        # For more info, look at: https://www.geeksforgeeks.org/python-dictionary-comprehension/

nums = [1,1,2,2,2,3]
test = Solution()
result = test.frequencySort(nums = nums)
print("Result: ", result)