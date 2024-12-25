class Solution:
    def gcdOfStrings(self, str1, str2):
        length_1 = len(str1)
        length_2 = len(str2)
        
        def valid(k): # Checks if the strings are divisible by k
            # print(f"length_1 % k: {length_1 % k}, length_2 % k: {length_2 % k}")
            if length_1 % k or length_2 % k: # Checks if the length of the strings is divisible by k
                # print("Returning False")
                return False
            n1, n2 = length_1 // k, length_2 // k
            base = str1[:k]
            return str1 == base * n1 and str2 == base * n2
        
        min_length = min(length_1, length_2)
        for i in range(min_length, 0, -1):
            if valid(i):
                return str1[:i]
        return ""

def testOne(test: Solution):
    str1 = "ABCABC"
    str2 = "ABC"
    print("Result from test 1: ", test.gcdOfStrings(str1, str2)) # Output: "ABC"

def testTwo(test: Solution):
    str1 = "ABABAB"
    str2 = "ABAB"
    print("Result from test 2: ", test.gcdOfStrings(str1, str2)) # Output: "ABC"



def main():
    test = Solution()
    testOne(test)
    testTwo(test)



if __name__ == "__main__":
    main()


