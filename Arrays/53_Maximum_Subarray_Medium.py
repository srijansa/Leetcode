import sys
from typing import List
class Solution:
    def  maxSubArray(self, nums: List[int]) -> int:
        """
        Check dp solution when free.
        Time Complexity-> O(n)
        kadane's algorithm
        """
        largest_sum=-sys.maxsize-1
        max_element=0
        for n in nums:
            max_element=max(n, n+max_element)
            largest_sum=max(largest_sum, max_element)
            print('Value of max-element: ',max_element,' Value of largest_sum: ', largest_sum)
        return largest_sum

def main():
    arr= sys.stdin.read().strip()
    nums=list(map(int, arr.strip('[]').replace('\n', ',').split(',')))
    sol=Solution()
    # print('Value of nums:', nums)
    largest_sum=sol.maxSubArray(nums)
    print(largest_sum)

if __name__=="__main__":
    main()