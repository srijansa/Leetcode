import sys
import ast
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

def main():
    input = '[[1,3],[2,6],[8,10],[15,18]]'
    #Answer for the above should be : [[1, 6], [8, 10], [15, 18]]
    intervals = ast.literal_eval(input)
    sol = Solution()
    merged = sol.merge(intervals)
    print(merged)

if __name__ == "__main__":
    main()
