class Solution:
    def findDuplicates(self, nums):
        sorted_list = sorted(nums)
        result = []
        for i in range(0, len(sorted_list) - 1) :
            if sorted_list[i] == sorted_list[i + 1]:
                result.append(sorted_list[i])
        return result 

#Some sample output
nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDuplicates(nums))
