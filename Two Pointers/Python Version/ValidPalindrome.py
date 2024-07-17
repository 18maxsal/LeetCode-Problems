# Link to Problem: https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = ""

        # Getting the letters and numbers ONLY from the given string
        for i in s:
            if i.isalpha():
                letters += i.lower()
            elif i.isdigit():
                letters += str(i)

        left = 0
        right = len(letters) - 1

        while left < right: # Iterating through both ends of the array until they meet in the middle 
            if letters[left] != letters[right]:
                return False
            left += 1
            right -= 1
        
        return True

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = "0P"
test = Solution()
result = test.isPalindrome(s = s)
print("Result: ", result)