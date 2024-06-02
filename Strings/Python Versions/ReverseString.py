class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # to_switch = len(s) - 1
        # end = len(s) // 2
        # for i in range(0, end):
        #     temp = s[to_switch]
        #     s[to_switch] = s[i]
        #     s[i] = temp
        #     to_switch = to_switch - 1
        
        end = len(s) // 2
        to_switch = len(s) - 1
        for i in range(0, end):
            s[i], s[to_switch] = s[to_switch], s[i] # Another way of swapping places without the use of a temp
            # variable

            to_switch -= 1

s = ["h", "e", "l", "l", "o"]
test = Solution()
print("before: ", s)
test.reverseString(s)
print("after: ", s)

        