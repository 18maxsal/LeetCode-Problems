# Link to Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0 # Pointer for the start of the array
        end = len(numbers) - 1 # Pointer for the end of the array 
        while start <= end: # Iterating through using a two pointer approach
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            
            elif numbers[start] + numbers[end] > target:  # I.E. our resulting number is greater than the target number, we 
                # can reduce this number by decreasing the index of the end pointer by one
                end -= 1
            else: # I.E. our resulting number is smaller than the target number, we can increase this number by 
                # increasing the index of the start pointer by one 
                start += 1