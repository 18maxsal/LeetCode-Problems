class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        validOpenCharacters = ["(", "{", "["]
        validClosingCharacters = [")", "}", "]"]

        for character in s:

            if character in validOpenCharacters: # We have an opening character with a possible match later on
                
                stack.append(validOpenCharacters.index(character))  # Appending the index of the opening character to 
                # The stack, used to avoid redundancy since the two lists containing either opening or closing characters 
                # Above have matches being the same index
            
            elif character in validClosingCharacters: # Closing character with a possible match from earlier
                 
                if len(stack) == 0: # Special Case: First character to check is a closing character
                    return False
                
                if character ==  validClosingCharacters[stack[-1]]: # Checking if current closing character matches the opening 
                    # character at the top of the stack, if so, then we pop it, otherwise return false
                    stack.pop()
                
                else:
                    return False
                
        return len(stack) == 0    
        
s = "()"
# s = "(]"
test = Solution()
result = test.isValid(s = s)
print(result)