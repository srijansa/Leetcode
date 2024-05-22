from typing import List
import sys
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        1. We use three pointers: left, right, and i.
        2. Everything revolves around the i pointer.
        3.The i pointer partitions the array into three sections: 0, 1, and 2.
        4.If i points to 0, it means we are on the left side, and the element is correctly placed. We swap it with the element at the left pointer, 
        as there might be a 1 at the left position. We then increment both left and i.
        5. If i points to 1, it means we are in the middle section, and we simply move to the next element by incrementing i.
        6. If i points to 2, we swap it with the element at the right pointer, as 2 needs to be placed at the end. We do not increment i in this case, 
        as the swapped element at the i position might also be a 2, requiring further action.
        """
        i, left, right= 0, 0, len(nums)-1
        while i<=right:
            if nums[i]==0:
                self.swap(i, left, nums)
                i+=1
                left+=1
            elif nums[i]==1:
                i+=1
            else:
                self.swap(i, right, nums)
                right-=1
        print(nums)

    def swap(self, i, j, nums:List[int])-> None:
        temp=nums[i]
        nums[i]=nums[j]
        nums[j]=temp
    

def main():
    arr= sys.stdin.read().strip()
    nums=list(map(int, arr.strip('[]').split(',')))
    sol=Solution()
    sol.sortColors(nums)

if __name__=="__main__":
    main()