class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}
        res, maxx = 0, float('-inf')
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 0
            hash_table[num] += 1

            if hash_table[num] > maxx:
                res = num
                maxx = hash_table[num]
        
        return res