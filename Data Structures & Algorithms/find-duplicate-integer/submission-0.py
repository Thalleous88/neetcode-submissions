class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for key, val in counts.items():
            if val > 1:
                return key
