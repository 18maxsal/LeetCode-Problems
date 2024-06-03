# Problem Link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/?envType=daily-question&envId=2024-06-03

class Solution:
    def appendCharacters(self, s, t):
        t_pointer = 0 # Points at the current char in t to compare with s
        matching_chars_t = 0 # Keeps track of how many letters are matching between
        # The two strings s and t

        for i in s:

            if matching_chars_t == len(t): # Checking to see if s is already a subset of t
                # before appending any characters to s, if so we simply return 0
                return 0
            
            if i == t[t_pointer]: # if there is a match in chars between both s and t, 
                # update any appropriate variables
                t_pointer += 1
                matching_chars_t += 1

        return len(t[t_pointer:]) # returning the length of letters needed to make s a subsequence of t
        