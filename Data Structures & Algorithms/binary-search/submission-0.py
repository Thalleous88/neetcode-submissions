class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        def bisearch(nums, target, left, right):

            if (right >= left):
                mid = left + (right - left) // 2
                if (nums[mid] == target):
                    return mid
                elif (nums[mid] > target):
                    return bisearch(nums, target, left, mid-1)
                else:
                    return bisearch(nums, target, mid+1, right)
            else:
                return -1

        res = bisearch(nums, target, 0, len(nums)-1)
        return res