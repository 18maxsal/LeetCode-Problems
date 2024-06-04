# Problem Link: https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04

class Solution:
    def longestPalindrome(self, s: str) -> int:
        to_return = 0 # The longest length of the palindrome is kept here
        chars_counts = self.counts(s)
        has_One = False # Used for the center part of the palindrome (i.e. the part of the palindrome with an 
        # odd number of chars)

        for i in chars_counts.keys():
            if chars_counts[i] % 2 == 0: # Checking if current letter frequency is even
                to_return += chars_counts[i]
            
            elif chars_counts[i] % 2 == 1 and has_One == False: 
                # Checking if current letter frequency is odd and has_One hasn't been set yet, 
                # if has_One hasn't been set yet, then we let the current letter represent the only
                # part of the palindrome with an odd number
                to_return += chars_counts[i]
                has_One = True
            
            else: # Current letter is odd and has_One has already been set 
                # Simply just make the current letter with an odd frequency even by subtracting 1
                to_return += chars_counts[i] - 1 

        return to_return
    
    # Responsible for getting the frequency of each letter in s
    def counts(self, s):
        to_return = {}
        for i in s:
            if i in to_return:
                value = to_return[i]
                to_return.update({i : value + 1})
            else:
                to_return.update({i : 1})

        return to_return


#s = "abccccdd"
# s = "a"
s = "bananas" # Expected result is 5 
test = Solution()
print(test.longestPalindrome(s))