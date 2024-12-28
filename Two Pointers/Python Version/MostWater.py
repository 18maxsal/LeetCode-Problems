# Problem link: https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def maxArea(self, height: list[int]): # NOTE: this is not as optimized because of the max function
        left = 0
        right = len(height) - 1
        best_area = self.calcArea(height, left, right)
        while left < right:
            temp_height = self.calcArea(height, left, right)
            best_area = max(best_area, temp_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best_area
    
    def maxArea_Optimized(self, height: list[int]): # This is a more optimized version of the solution
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            temp_area = 0
            if height[left] >= height[right]:
                temp_area = height[right] * (right - left)
                if max_area < temp_area:
                    max_area = temp_area
            
            elif height[right] > height[left]:
                temp_area = height[left] * (right - left)
                if max_area < temp_area:
                    max_area = temp_area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

    def calcArea(self, height: list[int], left: int, right: int):
        return (abs(right - left) * min(height[left], height[right]))

def testOne(test: Solution):
    height = [1,8,6,2,5,4,8,3,7]
    result = test.maxArea(height)
    # result = test.maxArea_Optimized(height)
    print(result)

def testTwo(test: Solution):
    height = [1, 1]
    result = test.maxArea(height)
    # result = test.maxArea_Optimized(height)
    print(result)


def main():
    test = Solution()
    testOne(test)
    testTwo(test)


if __name__ == "__main__":
    main()
