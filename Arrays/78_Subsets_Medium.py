from typing import List
import sys
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        I am not able to understand how the output is wrong. I understand my solution is incomplete by not able to proceed further on why my input is wrong. 
        """
        result=[[]]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    print('Value of i', i, 'Value of j: ', j)
                    arr=[]
                    arr.append(nums[j])
                    print('Value of arr: ', arr)
                    result.append(arr)
                    print('Value of result: ', result)
                else:
                    arr.append(nums[j])
                    if arr not in result:
                        result.append(arr)
        return result
    

def main():
    arr= sys.stdin.read().strip()
    nums=list(map(int, arr.strip('[]').replace('\n', ',').split(',')))
    sol=Solution()
    # print('Value of nums:', nums)
    largest_sum=sol.subsets(nums)
    print(largest_sum)

if __name__=="__main__":
    main()