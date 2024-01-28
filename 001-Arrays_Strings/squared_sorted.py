class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        squared_nums = [0] * len(nums)
        pointer = len(nums) -1 
        while (left<=right):
            
            if(abs(nums[left])> abs(nums[right])): 
                squared_nums[pointer] = nums[left]**2
                left = left + 1
            else:
                squared_nums[pointer] = nums[right]**2
                right = right - 1
            pointer = pointer - 1
        return squared_nums