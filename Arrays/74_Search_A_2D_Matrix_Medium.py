import sys
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        In the first solution I forgot that if the element doesn't exists in the range then just return False
        """
        i = 0
        while i < len(matrix):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[0]) - 1]:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
                return False  # I thought about it but missed it for a while 
            else:
                i += 1
        return False

def main():
    input=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target=16
    sol=Solution()
    answer=sol.searchMatrix(input, target)
    if answer==True:
        print('Element Found.')
    else:
        print('Element not Found.')

if __name__=='__main__':
    main()