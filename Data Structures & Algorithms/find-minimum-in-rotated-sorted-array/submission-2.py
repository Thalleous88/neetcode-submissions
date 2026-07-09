class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return

        if len(nums) == 1:
            return nums[0]

        def bisearch(l, r, arr):
            
            while (l <= r):
                mid = l + (r-l)//2
                if (l == r):
                    return arr[mid]

                if mid > 0 and arr[mid] < arr[mid-1]:
                    return arr[mid]
                elif arr[mid] > arr[r]:
                    l = mid+1
                else:
                    r = mid
                
        
        return bisearch(0, len(nums)-1, nums)
