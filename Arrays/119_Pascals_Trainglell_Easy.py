import sys
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        if rowIndex==0:
            return result
        left =0
        new_row=[1]
        for i in range(rowIndex):
            result=[0]+new_row+[0]
            new_row=[]
            left=0
            while left<len(result)-1:
                new_row.append(result[left]+result[left+1])
                left+=1
        return new_row

def main():
    input=int(sys.stdin.read().strip())
    sol=Solution()
    result=sol.getRow(input)
    print(result)

if __name__=='__main__':
    main()
    

