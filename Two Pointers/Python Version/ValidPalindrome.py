
class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ""
        # Getting the letters only from the given string
        for i in s:
            if i.isalpha():
                letters += i.lower()

        left = 0
        right = len(letters) - 1
        while left < right:
            if letters[left] == letters[right]:
                return False
            left += 1
            right -= 1
        
        return True

        # for i in range(len(letters) // 2):
        #     for j in range (len(letters) // 2, -1):
        #         if letters[i] != letters[j]:
        #             return False
        # return True

s = "A man, a plan, a canal: Panama"
# s = "race a car"
test = Solution()
result = test.isPalindrome(s = s)
print("Result: ", result)