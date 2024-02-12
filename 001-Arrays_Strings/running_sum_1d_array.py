class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = [nums[0]]
        for i in range (1,len(nums)):
            sum.append(sum[-1] + nums[i])
        return sums