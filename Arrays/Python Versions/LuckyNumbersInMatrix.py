
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        ans = []
        rows_and_columns = [] # Follows the following ordering: [row, column]
        for i in range(len(matrix)):
            rows_and_columns.append(matrix[i])
            column = []
            for j in range(len(matrix)):
                column.append(matrix[i][j])
            rows_and_columns.append(column)
        
        for i in rows_and_columns:
            pass    
        
        return ans
    
    def is_lucky(self, row, column, num):
        if min(row) == num and max(column) == num:
            return True
        return False







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