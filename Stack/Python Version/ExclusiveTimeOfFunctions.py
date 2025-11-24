from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n

        stack = []

        for index, vals in enumerate(logs):
            vals = vals.split(":")
            # print(vals)
            if vals[1] == "start":

                if stack:
                    diff = int(vals[2]) - int(stack[-1][1]) # Per units of time (differences works differently here)
                    ans[int(stack[-1][0])] += diff 

                    # temp additions:
                    top = stack.pop()
                    top[1] = vals[2]
                    stack.append(top)
                stack.append( [vals[0], vals[2]] ) # storing as: id, start_time
            
            # Case: vals[1] == "end"
            else:
                stack_vals = stack.pop()
                diff = int(vals[2]) - int(stack_vals[1]) + 1
                ans[int(stack_vals[0])] += diff

                # More temp additions: 
                if stack:
                    new_curr_top = stack.pop()
                    # new_curr_top[1] = stack_vals[1]
                    new_curr_top[1] = int(vals[2]) + 1
                    stack.append(new_curr_top)
                
        
        return ans

def testOne(test: Solution):
    n = 2
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    result = test.exclusiveTime(n, logs)
    print(result)

def testTwo(test: Solution):
    n = 1
    logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    result = test.exclusiveTime(n, logs)
    print(result)

def testThree(test: Solution):
    n = 2
    logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    result = test.exclusiveTime(n, logs)
    print(result)



def main():
    test = Solution()
    testOne(test)
    testTwo(test)
    testThree(test)


if __name__ == "__main__":
    main()