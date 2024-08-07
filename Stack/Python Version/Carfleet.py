# Link to Problem: https://leetcode.com/problems/car-fleet/
# Link to Solution Video (NeetCode): https://www.youtube.com/watch?v=Pr6T-3yB9RM
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        