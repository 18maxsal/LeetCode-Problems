class Solution:
    def smallestNumber(self, n: int) -> int:
        n = list(bin(n))
        n = n[2:]
        has_zero = False
        for i in range(len(n)):
            if n[i] == '0':
                has_zero = True
                n[i] = '1'
        return int("".join(n), 2)
    

def testOne(test = Solution()):
    n = 5
    result = test.smallestNumber(n)
    print(result)
    assert result == 7

def testTwo(test = Solution()):
    n = 10
    result = test.smallestNumber(n)
    print(result)
    assert result == 15

def testThree(test = Solution()):
    n = 3
    result = test.smallestNumber(n)
    print(result)
    assert result == 3




def main():
    test = Solution()
    testOne(test)
    testTwo(test)
    testThree(test)
    print("Passed tests")



if __name__ == "__main__":
    main()