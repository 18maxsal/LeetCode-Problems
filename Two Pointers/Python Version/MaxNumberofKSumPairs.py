class Solution():
    
    def maxOperations(self, nums: list[int], k: int):
        nums.sort()
        ans = 0
        counts = {}
        for i in nums: # Get all counts
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        keys = list(counts.keys())
        # print(counts.keys())
        # print("keys: ", keys)
        print("Counts: ", counts)
        left =  0
        right = len(keys) - 1
        while left < right:
            if keys[left] <= k:
                break
            # print(f"keys[left]: {keys[left]}, keys[right]: {keys[right]}")
            if keys[left] + keys[right] == k and counts[keys[left]] >= 1 and counts[keys[right]] >= 1:
                if counts[keys[right]] > counts[keys[left]]:
                    counts[keys[right]] = counts[keys[right]] - counts[keys[left]]
                    ans += counts[keys[left]]
                    counts[keys[left]] = 0
                    left += 1
                    if (keys[right] * 2) == k and counts[keys[right]] > 2:
                        remainder = counts[keys[right]] % 2
                        ans += counts[keys[right]] // 2
                        counts[keys[right]] = remainder
                
                else:
                    counts[keys[left]] = counts[keys[left]] - counts[keys[right]]
                    ans += counts[keys[right]]
                    counts[keys[right]] = 0
                    right -= 1
                    if keys[left] * 2 == k and counts[keys[left]] > 2:
                        remainder = counts[keys[left]] % 2
                        ans += counts[keys[left]] // 2
                        counts[keys[left]] = remainder
                continue
            
            if keys[right] * 2 == k and counts[keys[right]] > 2:
                        remainder = counts[keys[right]] % 2
                        ans += counts[keys[right]] // 2
                        counts[keys[right]] = remainder
            
            elif keys[left] * 2 == k and counts[keys[left]] > 2:
                        remainder = counts[keys[left]] % 2
                        ans += counts[keys[left]] // 2
                        counts[keys[left]] = remainder
                


            if keys[left] + keys[right] > k:
                right -=1
            elif keys[left] + keys[right] < k:
                left +=1

        return ans


def testOne(test: Solution):
    pass

def testTwo(test: Solution):
    pass

def main():
    test = Solution()
    testOne(test)
    testTwo(test)

if __name__ == "__main__":
    main()