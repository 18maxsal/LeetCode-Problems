# Link to problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        signs = "-+/*"

        for i in tokens:
            
            if i in signs: 
                # Essentially, when we find the matching sign in i, we just pop the top 2 elements in the stack, 
                # Perform the appropriate operation, and then put the result back to the top of the stack.  We 
                # Should end up with only 1 element left at the end of the for loop, which is our final answer.
                if i == "+":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 + num1)
                elif i == "-":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 - num1)
                elif i == "/":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(int(num2 / num1))
                elif i == "*":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 * num1)
            else:
                stack.append(i)
        return int(stack.pop())

# tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
test = Solution()
result = test.evalRPN(tokens)
print(result)