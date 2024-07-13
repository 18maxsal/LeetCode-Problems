# Link to Problem: https://leetcode.com/problems/car-fleet/
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        stack = [] # Will be a single array containing both the position, speed, and the time it will
        # take to reach the target for any i'th car

        for i in range(len(position)): # Combining position and speed arrays into one single array
            time_till_target = target - position[i]
            stack.append(position[i], speed[i], time_till_target)
        