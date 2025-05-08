# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/

import heapq
import random
from typing import List
from collections import Counter # Used in heap solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution that I came up with (works efficiently, but there are different solutions)
        counts = {}
        ans = []
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        sorted_counts = dict(sorted(counts.items(), key = lambda item: item[1], reverse = True))
        to_break = 0
        for i in sorted_counts.keys():
            if to_break == k:
                break
            else:
                ans.append(i)
                to_break += 1
        return ans
    
    def topKFrequentHeap (self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)
    
    def topKFrequentQuickSelect(self, nums: List[int], k: int) -> List[int]:
        # Solution from LeetCode writeup, appears to be the optimal solution
        # TODO: Look over
        count = Counter(nums)
        unique = list(count.keys())
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            unique[right], unique[store_index] = unique[store_index], unique[right]
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            if left == right:
                return
            
            pivot_index = random.randint(left, right)

            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            
            else:
                quickselect(pivot_index + 1, right, k_smallest)
            
        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[n - k:]




def test_one(test: Solution):
    nums = [1,1,1,2,2,3]
    k = 2
    print(f"Result from test one: {test.topKFrequent(nums, k)}")

def test_two(test: Solution):
    nums = [1]
    k = 1
    print(f"Result from test two: {test.topKFrequent(nums, k)}")

def main():
    test = Solution()
    test_one(test)
    test_two(test)

if __name__ == "__main__":
    main()