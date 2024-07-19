# Link to Problem: https://leetcode.com/problems/lucky-numbers-in-a-matrix/?envType=daily-question&envId=2024-07-19
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        # ans = []
        # rows_and_columns = [] # Follows the following ordering: [row, column]
        # for i in range(len(matrix)):
        #     row = []
        #     column = []
        #     for j in range(len(matrix)):
        #         row.append(matrix[i][j])
        #         column.append(matrix[j][i])
        #     rows_and_columns.append([row, column])

        ans = []
        nums_found = []
        for i in range(len(matrix)):
            row_min = []
            column_max = []
            for j in range(len(matrix)):
                row_min.append(matrix[i][j])
                column_max.append(matrix[j][i])
            nums_found.append([min(row_min), max(column_max)])
        
        for i in nums_found:
            if i[0] == i[1]:
                ans.append(i[0])
        return ans
    
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