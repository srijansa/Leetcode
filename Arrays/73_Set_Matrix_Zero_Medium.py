from typing import List
import ast

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        This function modifies the input matrix such that if an element is 0,
        its entire row and column are set to 0. The modification is done in place.
        The first row and first column are used as markers to keep track of which
        rows and columns need to be zeroed. Additionally, two flags are used to 
        remember if the first row and first column originally contained any zeros.
        Modifying the first row and the first column to check the if any zeroes 
        exists in it. 
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        #Flags to check if the first row and first column contain any zeros
        row_zero = False
        col_zero = False
        
        #Check if the first column has any zeros - We can't modify the first row or column at first 
        for i in range(rows):
            if matrix[i][0] == 0:
                col_zero = True
                break
        
        #Check if the first row has any zeros
        for j in range(cols):
            if matrix[0][j] == 0:
                row_zero = True
                break
        
        #Use the first row and column as markers for rows and columns that should be zeroed
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        #Zero out cells based on the markers in the first row and column
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
        
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        
        #If the first row originally had any zeros, zero out the entire first row
        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        #If the first column originally had any zeros, zero out the entire first column
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0

def main():
    import sys
    input = sys.stdin.read().strip()
    matrix = ast.literal_eval(input)
    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)

if __name__ == "__main__":
    main()
