from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        for window_size in range(1, n + 1):
            curr_total = 0
            left, right = 0, 0
            curr_size = 0
            while right < n:
                
                if curr_size < window_size:
                    curr_total += nums[right]
                    right += 1
                    curr_size += 1

                    if curr_total >= target:
                        return window_size
                
                else:
                    curr_total -= nums[left]
                    curr_size -= 1
                    left += 1
        
        return 0
    
    def minSubArrayLenOptimized(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0

def testOne(test: Solution):
    nums = [2,3,1,2,4,3]
    target = 7
    result = test.minSubArrayLen(target, nums)
    print(result)
    assert result == 2

def testTwo(test: Solution):
    nums = [1,4,4]
    target = 4
    result = test.minSubArrayLen(target, nums)
    # result = test.minSubArrayLen(target, nums)
    print(result)
    assert result == 1

def testThree(test: Solution):
    nums = [1,1,1,1,1,1,1,1]
    target = 11
    result = test.minSubArrayLen(target, nums)
    print(result)
    assert result == 0

def testFour(test: Solution):
    nums = [1,2,3,4,5]
    target = 11
    result = test.minSubArrayLen(target, nums)
    print(result)
    assert result == 3

def testFive(test: Solution):
    nums = [1,2,3,4,5]
    target = 15
    result = test.minSubArrayLen(target, nums)
    print(result)
    assert result == 5


def main():
    test = Solution()
    testOne(test)
    testTwo(test)
    testThree(test)
    testFour(test)
    testFive(test)


if __name__ == "__main__":
    main()