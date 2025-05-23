# Link to problem: https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str): # Using a two pointer approach here
        left = 0
        right = len(s) - 1
        vowels = "aeiouAEIOU"
        s = list(s)
        while left <= right:
            if s[left] in vowels and s[right] in vowels: # Case of where the left and right pointer are pointing at vowels
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                continue
            elif s[left] in vowels and s[right] not in vowels: # Case of only left pointer is pointing at a vowel
                while left <= right and s[right] not in vowels:
                    right -= 1
                continue
            elif s[left] not in vowels and s[right] in vowels: # Case of only right pointer is pointing at a vowel
                while left <= right and s[left] not in vowels:
                    left += 1
                continue
            else: # Case of NEITHER the left or right pointer is pointing at a vowel
                left += 1
                right -= 1
        return "".join(s)

def testOne(test: Solution):
    s = "IceCreAm"
    print("TEST ONE: ")
    print(f"Word before reversing vowels: {s}")
    result = test.reverseVowels(s)
    print(f"Word after reversing vowels: {result}")
    print("")

def testTwo(test: Solution):
    s = "leetcode"
    print("TEST TWO: ")
    print(f"Word before reversing vowels: {s}")
    result = test.reverseVowels(s)
    print(f"Word after reversing vowels: {result}")
    print("")




def main():
    test = Solution()
    testOne(test)
    testTwo(test)

if __name__ == "__main__":
    main()