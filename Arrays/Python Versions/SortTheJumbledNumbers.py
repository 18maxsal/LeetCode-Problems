# Problem Link: https://leetcode.com/problems/sort-the-jumbled-numbers/?envType=daily-question&envId=2024-07-24
from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new_nums = []

        for i, n in enumerate(nums): # Converting to the mapped numbers system
            new_nums.append((int(self.jumbledNumber(mapping, str(n))), i))
        
        new_nums.sort()
        ans = []
        for i in new_nums:
            ans.append(nums[i[1]])

        return ans

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