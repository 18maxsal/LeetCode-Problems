from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # counts = {}
        ans = []
        endAppend = []
        # for i in arr1:
        #     if i in counts:
        #         value = counts[i]
        #         counts.update({ i : value + 1})
        #     else:
        #         counts.update({ i : 1})
        # print(counts)
        counts = self.getCounts(arr1)

        for i in arr2:
            if i in counts:
                for j in range(0, counts[i]):
                    ans.append(i)
            else:
                endAppend.append(i)
        
        print(endAppend)
        for i in endAppend:
            ans.append(i)

        arr1.sort()

        for i in arr1:
            if i not in ans:
                for j in range(0, counts[i]):
                    ans.append(i)

        return ans
    
    def getCounts(self, arr1):
        counts = {}
        for i in arr1:
            if i in counts:
                value = counts[i]
                counts.update({ i : value + 1})
            else:
                counts.update({ i : 1})
        return counts


arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]
test = Solution()
ans = test.relativeSortArray(arr1 = arr1, arr2 = arr2)
print(ans) 
