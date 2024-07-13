# Link to Problem: https://leetcode.com/problems/car-fleet/
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        stack = [] # Will be a single array containing both the position and speed of any i'th car

        for i in range(len(position)): # Combining position and speed arrays into one single array
            stack.append(position[i], speed[i])
        