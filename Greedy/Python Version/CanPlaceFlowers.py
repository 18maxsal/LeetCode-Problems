# Problem Link: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        counter = 0

        for i in range(0, len(flowerbed)):
            
            if flowerbed[i] == 0: # Checks if current plot is 0

                empty_left = (i == 0) or flowerbed[i - 1] == 0 # Checking to see if the current plot is at the beginning of 
                # the list OR if the element before the current one is 0

                empty_right = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0 # Checking to see if the current plot is at the end of 
                # the list OR if the element after the current one is 0

                if empty_left and empty_right: # Checking to see if both the plots before and after the current one are 
                    # 0's
                    counter += 1
                    flowerbed[i] = 1
        
        return counter >= n

# flowerbed = [1,0,0,0,1]
flowerbed = [1,0,0,0,1,0,0]
n = 2
test = Solution()
result = test.canPlaceFlowers(flowerbed, n)
print(result)