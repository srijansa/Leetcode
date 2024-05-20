import sys
from typing import List
#Use the following to execute: echo 5 | python 118_Pascals_Triangle_Easy.py
class Solution: 
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = [[1]]
        for i in range(1, numRows):
            temp = [0] + result[-1] + [0]
            newRow = []
            # print('checking the last row: '+str(result[-1]))
            for j in range(len(result[-1]) + 1):
                newRow.append(temp[j] + temp[j + 1])
            result.append(newRow)
        return result 
    
def main():
    n = int(sys.stdin.read().strip())
    result = Solution()
    matrix = result.generate(n)
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
