# Problem Link: https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in ans:
                ans[sorted_str].append(i)
            else:
                ans[sorted_str] = []
                ans[sorted_str].append(i)
        to_return = []
        for i in ans.keys():
            to_return.append(ans[i])
        return to_return        

def test_one(test: Solution):
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"Result from test one: {test.groupAnagrams(strs)}")

def test_two(test: Solution):
    strs = [""]
    test.groupAnagrams(strs)
    print(f"Result from test two: {test.groupAnagrams(strs)}")
    
def test_three(test: Solution):
    strs = ["a"]
    print(f"Result from test three: {test.groupAnagrams(strs)}")

def main():
    test = Solution()
    test_one(test)
    test_two(test)


if __name__ == "__main__":
    main()