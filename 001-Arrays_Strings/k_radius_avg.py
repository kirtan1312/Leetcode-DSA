class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if(k ==0 ):
            return nums 
        
        if(k*2+1>len(nums)):
            return [-1] * len(nums)
  
        prefix = [nums[0]]
        for i in range (1,len(nums)):
            prefix.append(prefix[-1] + nums[i])     
            
        kavg = [-1] * k
        kavg.append(prefix[k*2]//(k*2+1))
        n = 0
        for i in range (k*2+1, len(nums)): 
            total = prefix[i] - prefix[n] 
            kavg.append(total//(k*2+1))
            n += 1
            
        arr = [-1] * k
        kavg += arr
        
        return kavg
            
            