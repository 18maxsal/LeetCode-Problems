# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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