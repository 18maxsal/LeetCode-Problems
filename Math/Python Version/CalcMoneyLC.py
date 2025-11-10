


class Solution:
    def totalMoney(self, n: int) -> int:
        prev_monday = 0
        ans = 0
        prev_day = 0
        for i in range(1, n + 1):
            if i == 1 or i % 7 == 1:
                prev_monday += 1
                print(f"adding {prev_monday}")
                ans += prev_monday
                prev_day = prev_monday
            else:
                prev_day += 1
                print(f"adding {prev_day}")
                ans += prev_day
        return ans



def testOne(test: Solution):
    n = 4
    res = test.totalMoney(n)
    print(f"Result: {res}")

def testTwo(test: Solution):
    n = 10
    res = test.totalMoney(n)
    print(f"Result: {res}")

def testThree(test: Solution):
    n = 20
    res = test.totalMoney(n)
    print(f"Result: {res}")





def main():
    test = Solution()
    testOne(test)
    testTwo(test)
    testThree(test)


if __name__ == "__main__":
    main()