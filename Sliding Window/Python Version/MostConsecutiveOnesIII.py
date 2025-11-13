# Problem Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def largestOnes(self, nums: list[int], k: int):

        left = 0
        right = 0
        while right < len(nums): 
            if nums[right] == 0:
                k -= 1
            right += 1
            if k < 0:
                if nums[left] == 0: # Used to ensure we have k zero's in our window
                    k += 1
                left += 1
        return right - left


def testOne(test: Solution):
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    result = test.largestOnes(nums, k) 
    print(f"Result from test one: {result}, Expected: 6" )

def testTwo(test: Solution):
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    result = test.largestOnes(nums, k)
    print(f"Result from test two: {result}, Expected: 10" )


def main():
    test = Solution()
    testOne(test)
    testTwo(test)


if __name__ == "__main__":
    main()

