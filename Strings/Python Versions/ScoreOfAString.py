# This problem is from LC: https://leetcode.com/problems/score-of-a-string/?envType=daily-question&envId=2024-06-01
# Problem is Titled "3110. Score of a String"
string = "hello"
string_ascii = []
for i in string: # Converting the given string into its ASCII values
    # print("letter: ", i)
    # print("ascii: ", ord(i))
    string_ascii.append(ord(i))

print(string_ascii)
ans = []

for i in range(1, len(string_ascii)):
    # Calculating the absolute difference between ASCII values of adjacent characters
    result = abs( string_ascii[i] - string_ascii[i - 1])
    print(result)
    ans.append(result)
print(sum(ans)) # Answer is found here