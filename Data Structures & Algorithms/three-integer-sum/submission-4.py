class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        l = len(nums)
        marked = set()

        res = []
        

        for i in range(l-1):
            if nums[i] in marked:
                continue

            target = 0 - nums[i]
            left, right = i+1, l-1

            while left < right:
                temp = nums[left] + nums[right]
                if temp == target:
                    r = [nums[i], nums[left], nums[right]]
                    if tuple(r) in marked:
                        left += 1
                        right -= 1
                        continue
                    
                    res.append(r)
                    marked.add(tuple(r))

                    left += 1
                    right -= 1
                elif temp > target:
                    right -= 1
                else:
                    left += 1

            marked.add(nums[i])

            

        return res
        