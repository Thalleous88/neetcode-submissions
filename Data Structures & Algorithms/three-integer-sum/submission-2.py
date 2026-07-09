class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            l = len(nums)-1
            i = index+1

            complement = 0 - num

            while (i < l):
                temp = complement - nums[i] - nums[l]

                if temp == 0:
                    res.append([num, nums[i], nums[l]])
                    i += 1
                    l -= 1

                    while i < l and nums[i] == nums[i-1]:
                        i += 1
                    
                    while i < l and nums[l] == nums[l+1]:
                        l -= 1

                elif temp < 0:
                    l -= 1
                else:
                    i += 1



        return res
                