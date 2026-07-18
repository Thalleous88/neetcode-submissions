class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bisearch(left, right):

            while left <= right:
                mid = (left + right)//2

                
                if nums[mid] == target:
                    return mid
                elif len(nums) % 2 == 0 and mid+1 >= 0 and mid+1 < len(nums) and nums[mid+1] == target:
                    return mid+1
                elif nums[left] == target:
                    return left
                elif left+1 < len(nums) and nums[left+1] == target:
                    return left+1
                elif right-1 >= 0 and nums[right-1] == target:
                    return right-1
                elif nums[right] == target:
                    return right
                
                if abs(target-nums[left]) < abs(target-nums[right]):
                    right = mid-1
                else:
                    left = mid+1

            if right < left:
                return -1

        return bisearch(0, len(nums)-1)

                