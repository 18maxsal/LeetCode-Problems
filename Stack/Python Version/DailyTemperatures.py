# Problem Link: https://leetcode.com/problems/daily-temperatures/submissions/1319275203/
from typing import List
class Solution:
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures) # Creating a list with len(temperatures) 0's
        
        stack = [] #Contains a pair for each index (index, temperature)

        for i, t in enumerate(temperatures):
            # For more info on enumerate in python:
            # refer to https://www.geeksforgeeks.org/enumerate-in-python/

            while stack and t > stack[-1][1]:
                # While our stack is NOT empty and our current temperature t is 
                # greater than the temperature on the top of the stack...
                stackIndex, stackTemp = stack.pop()
                ans[stackIndex] = i - stackIndex
            stack.append([i, t]) 
        return ans

temperatures = [73,74,75,71,69,72,76,73]
test = Solution()
result = test.dailyTemperatures(temperatures)
print(result)

        