# Link to Problem: https://leetcode.com/problems/lucky-numbers-in-a-matrix/?envType=daily-question&envId=2024-07-19
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        # Used from the fact that there can be AT MOST only 1 lucky number,
        # NOTE: look at editorial of this problem for more info
        N, M = len(matrix), len(matrix[0]) # The dimensions of the matrix (M * N)

        r_min_max = float('-inf')
        for i in range(N): # Gets the biggest number across all rows
            r_min = min(matrix[i])  
            r_min_max = max(r_min_max, r_min)

        c_max_min = float('inf')
        for i in range(M): # Gets the smallest number across all columns
            c_max = max(matrix[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []
    
    def is_lucky(self, row, column, num):
        if min(row) == num and max(column) == num:
            return True
        return False


matrix = [[3,7,8],[9,11,13],[15,16,17]]
test = Solution()
result = test.luckyNumbers(matrix= matrix)

print(result)




# arr = [[1, 2, 3], 
#        [4, 5, 6],
#        [7, 8, 9]]

# row_and_column = []
# for i in range(len(arr)): # iterates through each column
#     # print(arr[0][i])
#     row = []
#     column = []
#     for j in range(len(arr)): # iterates through each row
#         row.append(arr[i][j])
#         print(arr[i][j])
#         column.append(arr[j][i])
#     print("current row: ", row)
#     print("current column: ", column)

# # print(arr)