# Problem Link: https://leetcode.com/problems/fruit-into-baskets/

from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        basket = {}
        left, right = 0, 0
        ans = 0
        current_count = 0
        while right < n:

            if fruits[right] in basket: # Checking if the current fruit is in our basket, if so, then add to our count
                basket[fruits[right]] += 1
                right += 1
                current_count += 1
            
            else:

                basket[fruits[right]] = 1
                if len(basket) > 2:
                    # to_keep = fruits[right - 1]
                    ans = max(ans, current_count)
                    while len(basket) > 2:
                        basket[fruits[left]] -= 1
                        current_count -= 1
                        if basket[fruits[left]] == 0:
                            basket.pop(fruits[left])
                        left += 1
                current_count += 1

                right += 1

            



def main():
    test = Solution()

if __name__ == "__main__":
    main()