from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] != 0:
                total += nums[i]
            
            else:
                other_side = 0
                for j in range(i, n):
                    if nums[j] != 0:
                        other_side += nums[j]
                if total == other_side:
                    ans += 2
                elif total == (other_side + 1):
                    ans += 1
                elif (total + 1) == other_side:
                    ans += 1
        return ans
    
def testOne(test: Solution):
    nums = [1,0,2,0,3]
    result = test.countValidSelections(nums)
    print(result)
    assert result == 2

def testTwo(test: Solution):
    nums = [2,3,4,0,4,1,0]
    result = test.countValidSelections(nums)
    print(result)
    assert result == 0

def testThree(test: Solution):
    nums = [16,13,10,0,0,0,10,6,7,8,7]
    result = test.countValidSelections(nums)
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