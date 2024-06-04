# Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        ans = []
        new_nums = list(set(nums))
        new_nums.sort()
        curr_consecutive = []
        
        for i in range(0, len(new_nums) - 1):

            if new_nums[i] + 1 == new_nums[i + 1]: # Found consecutive numbers
                curr_consecutive.append(new_nums[i])
                curr_consecutive.append(new_nums[i + 1])
            
            else: # Found the end of the consecutive numbers list
                # Will add the found list to answer list and then clearing the curr_consecutive array
                if len(curr_consecutive) > 1:
                    ans.append(list(set(curr_consecutive)))
                
                curr_consecutive.clear()

        if len(curr_consecutive) > 1: # Special case: the entire list is consecutive
            ans.append(list(set(curr_consecutive)))
        
        max_length = 0

        for i  in ans: # Finding the length of the longest length of consecutive numbers
            if len(i) > max_length:
                max_length = len(i)

        if len(ans) == 0: # Handling more special cases 
            if len(nums) == 0: # We are given an empty list
                return 0
            else: # There are no consecutive numbers, but given list is not empty
                return 1
            
        return max_length
    
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [100,4,200,1,3,2]
nums = [0]
test = Solution()
print(test.longestConsecutive(nums))       