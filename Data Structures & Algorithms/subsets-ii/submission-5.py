class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        l = len(nums)
        nums.sort()
        res = []
        res.append([])

        def subset(temp, index, nums):
            if index >= l:
                return

      
            for i in range(index, l):
                if i > index and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                res.append(list(temp))
                subset(temp, i+1, nums)
                
                

                temp.pop()

        subset([], 0, nums)
   
        return res

            
