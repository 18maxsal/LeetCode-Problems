# Problem Link: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/?envType=daily-question&envId=2025-10-23

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            new_s = ""

            for i in range(1, len(s)):
                new_s += str((int(s[i]) + int(s[i - 1])) % 10)
            s = new_s
            # print(s)
        if len(s) != 2:
            return False


        return s[0] == s[1]


def testOne(test: Solution):
    s = "3902"
    result = test.hasSameDigits(s)
    print(result)
    assert result == True


def testTwo(test: Solution):
    s = "34789"
    result = test.hasSameDigits(s)
    print(result)
    assert result == False



def main():
    test = Solution()
    testOne(test)
    testTwo(test)


if __name__ == "__main__":
    main()


