# Link to Problem: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=daily-question&envId=2024-08-05

from typing import List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        strings = {} 
        for i in arr: # Getting counts of all strings in arr
            if i in strings:
                strings[i] += 1
            else:
                strings[i] = 1
        
        distinct_strings = []
        for i in strings.keys(): # Appending strings that have a value of 1 in the dictionary 
            # This indicates that the string is unique
            if strings[i] == 1:
                distinct_strings.append(i)

        if len(distinct_strings) < k: # Ensuring that there are more than k distinct strings
            return ""
        return distinct_strings[k - 1]

arr = ["d","b","c","b","c","a"]
k =  2
test = Solution()
result = test.kthDistinct(arr = arr, k = k)
print(result)