# Link to problem: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        s = s.split(" ")
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "":
                ans += s[i] + " "
        return ans.strip()

def testOne(test: Solution):
    s = "the sky is blue"
    print(f"String before reversing words: {s}")
    result = test.reverseWords(s)
    print(f"String after reversing words: {result}")
    print("")

def testTwo(test: Solution):
    s = "  hello world  "
    print(f"String before reversing words: {s}")
    result = test.reverseWords(s)
    print(f"String after reversing words: {result}")
    print("")

def testThree(test: Solution):
    s = "a good   example"
    print(f"String before reversing words: {s}")
    result = test.reverseWords(s)
    print(f"String after reversing words: {result}")
    print("")


def main():
    test = Solution()
    testOne(test)
    testTwo(test)
    testThree(test)



if __name__ == "__main__":
    main()