class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        minnum = min(nums[0],0)
        for i in range (1, len(nums)):
           #minnum = min(minnum,prefix[-1])
           prefix.append(prefix[-1] + nums[i])  
           minnum = min(minnum,prefix[-1])
        return -minnum+1 