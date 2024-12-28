class Solution:
    def maxArea(self, height: list[int]):
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

    def calcArea(self, height: list[int], left: int, right: int):
        return (abs(right - left) * min(height[left], height[right]))

def testOne(test: Solution):
    height = [1,8,6,2,5,4,8,3,7]
    result = test.maxArea(height)
    print(result)

def testTwo(test: Solution):
    height = [1, 1]
    result = test.maxArea(height)
    print(result)


def main():
    test = Solution()
    testOne(test)
    testTwo(test)


if __name__ == "__main__":
    main()
