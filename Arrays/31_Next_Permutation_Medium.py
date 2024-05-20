from typing import List
import sys
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges the elements into the next lexicographically greater permutation.
        If no such permutation exists, it rearranges into the lowest possible order.
        The replacement must be in place and use only constant extra memory.
        Use: echo "[1, 1, 5]" | python 31_Next_Permutation_Medium.py to run for test case [1, 1, 5] Output should be [1, 5, 1]
        """
        if len(nums) <= 1:
            return
        
        #Step 1: Find the largest index `last_index` such that `nums[last_index] < nums[last_index + 1]`
        last_index = len(nums) - 2
        while last_index >= 0 and nums[last_index] >= nums[last_index + 1]:
            last_index -= 1
        
        if last_index >= 0:
            #Step 2: Find the largest index `index` such that `nums[index] > nums[last_index]`
            for i in range(len(nums) - 1, last_index, -1):
                if nums[i] > nums[last_index]:
                    index = i
                    break
            #Step 3: Swap the values of `nums[last_index]` and `nums[index]`
            nums[last_index], nums[index] = nums[index], nums[last_index]
        
        #Step 4: Reverse the subarray `nums[last_index + 1:]`
        left, right = last_index + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

def main():
    input= sys.stdin.read().strip()
    nums=list(map(int, input.strip('[]').split(',')))
    sol=Solution()
    sol.nextPermutation(nums)
    print(nums)

if __name__=="__main__":
    main()