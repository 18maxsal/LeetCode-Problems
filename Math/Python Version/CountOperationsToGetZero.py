

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            ans += 1

        return ans
    

def testOne(test: Solution):
    num1 = 2
    num2 = 3
    result = test.countOperations(num1, num2)
    print(f"Result: {result}")
    assert result == 3

def testTwo(test: Solution):
    num1 = 10
    num2 = 10
    result = test.countOperations(num1, num2)
    print(f"Result: {result}")
    assert result == 1



def main():
    test = Solution()
    testOne(test)
    testTwo(test)

if __name__ == "__main__":
    main()