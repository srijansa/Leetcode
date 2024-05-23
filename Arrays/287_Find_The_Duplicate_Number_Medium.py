import sys
from typing import List
class Solution:
    def findDuplicates(self, nums:List[int])-> int:
        """
        1. We are just checking the element that is repeating again using hashmaps.
        2. Use echo [1,3,4,2,2] | python 287_Find_The_Duplicate_Number_Medium.py -> Answer should be 2
        """
        result={}
        for n in nums:
            if n not in result.keys():
                result[n]=1
            else:
                return n

def main():
    input_val=sys.stdin.read().strip()
    nums = list(map(int, input_val.strip('[]').replace('\n', ',').split(',')))
    sol=Solution()
    n=sol.findDuplicates(nums)
    print(n)

if __name__=="__main__":
    main()