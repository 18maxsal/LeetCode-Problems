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

    def canPlaceFlowers_Another_Solution(self, flowerbed, n):
        counter = 0
        for i in range(len(flowerbed)):
            if i == 0  and i + 1 < len(flowerbed) and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                counter += 1
            elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                counter += 1
            elif flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                counter += 1
            if counter >= n:
                return True
        return False


def testOne(test: Solution):
    flowerbed = [1,0,0,0,1]
    n = 2
    print(f"flowerbed from test one: {flowerbed}, n: {n}")
    result = test.canPlaceFlowers(flowerbed, n)
    # result = test.canPlaceFlowers_Another_Solution(flowerbed, n)
    print("Result from test One: ", result)
    if result:
        print(f"Resulting flowerbed: {flowerbed}")
    print("")

def testTwo(test: Solution):
    flowerbed = [1,0,0,0,1,0,0]
    n = 2
    print(f"flowerbed from test two: {flowerbed}, n: {n}")
    result = test.canPlaceFlowers(flowerbed, n)
    # result = test.canPlaceFlowers_Another_Solution(flowerbed, n)
    print("Result: ", result)
    if result:
        print(f"Resulting flowerbed: {flowerbed}")
    print("")


def testThree(test: Solution):
    flowerbed = [0,0,0,0,1]
    n = 2
    print(f"flowerbed from test three: {flowerbed}, n: {n}")
    result = test.canPlaceFlowers(flowerbed, n)
    # result = test.canPlaceFlowers_Another_Solution(flowerbed, n)
    print("Result: ", result)
    if result:
        print(f"Resulting flowerbed: {flowerbed}")
    print("")


def main():
    test = Solution()
    testOne(test)
    testTwo(test)
    testThree(test)

if __name__ == "__main__":
    main()