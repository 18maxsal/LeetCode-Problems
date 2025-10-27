

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        devices_row = []
        for row in bank:
            curr_devices = 0
            for i in row:
                if i == "1":
                    curr_devices += 1
            if curr_devices > 0:
                devices_row.append(curr_devices)
        
        for i in range(1, len(devices_row)):
            ans += devices_row[i - 1] * devices_row[i]
        
        return ans
    

def testOne(test: Solution):
    bank = ["011001","000000","010100","001000"]
    result = test.numberOfBeams(bank) 
    print(result)
    assert result == 8
    

def testTwo(test: Solution):
    bank = ["000","111","000"]
    result = test.numberOfBeams(bank) 
    print(result)
    assert result == 0




def main():
    test = Solution()
    testOne(test)
    testTwo(test)


if __name__ == "__main__":
    main()