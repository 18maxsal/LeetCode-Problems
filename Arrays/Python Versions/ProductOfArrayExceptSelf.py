# Link to Problem: https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def productExceptSelf(self, nums: list[int]):
        prefixAndPostfixArray = []
        runningProduct = 1
        prefixAndPostfixArray.append(runningProduct)
        # Processing prefix array
        
        for i in range(1, len(nums)): # Traversing Array from left to Right
            runningProduct*=nums[i-1]
            prefixAndPostfixArray.append(runningProduct)
        runningProduct = 1
        print(prefixAndPostfixArray)

        #Processing postfix array
        for i in range(len(nums)-1, -1, -1): # Traversing Array from right to left
            prefixAndPostfixArray[i]*=runningProduct
            runningProduct*=nums[i]
        print(prefixAndPostfixArray)
        return prefixAndPostfixArray
    
def testOne(test: Solution):
    nums = [1,2,3,4]
    print("TEST 1:")
    print(f"nums: {nums}")
    result = test.productExceptSelf(nums)
    print(f"Result: {result}\n")

def testTwo(test: Solution):
    nums = [-1,1,0,-3,3]
    print("TEST 2:")
    print(f"nums: {nums}")
    result = test.productExceptSelf(nums)
    print(f"Result: {result}\n")

def main():
    test = Solution()
    testOne(test)
    testTwo(test)

if __name__ == "__main__":
    main()