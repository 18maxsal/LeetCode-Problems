class Solution:

    def beautifulSubsets(self, nums, k):
        counter = 0
        partitions = []
        subset = []
        nums.sort()
        self.getPartitions(partitions, subset, nums, 0)
        for i in partitions:
            if len(i) == 0:
                continue
            if len(i) == 1 and k != 0:
                counter += 1
            else:
                isBeautiful = self.absoluteDifference(i, k)
                if isBeautiful:
                    counter += 1
        return counter
    
    def getPartitions(self, partitions, subset, nums, index):
        partitions.append(subset[:])
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.getPartitions(partitions, subset, nums, i+1)
            subset.pop()

    def absoluteDifference(self, arr, k):
        for i in range(1, len(arr) + 1):
            if abs(arr[i] - arr[i - 1]) == k:
                return False
            return True

test = Solution()
result = test.beautifulSubsets([2, 4, 6], 2)
# print(test.beautifulSubsets([2, 4, 6], 2))
print("result with [2, 4, 6] and k = 2: ", result)
result = test.beautifulSubsets([4,2,5,9,10,3], 1) 
print("result with [4,2,5,9,10,3] and k = 1: ", result)