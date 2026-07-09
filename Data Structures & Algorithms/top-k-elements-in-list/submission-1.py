class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        hset = set(nums)
        thisdict = {}
        for a in hset:
            thisdict.update({a: nums.count(a)})

        sorted_dict = dict(sorted(thisdict.items(), key=lambda x:x[1]))

        b = len(sorted_dict)

        for i in range(b):
            if k != b:
                sorted_dict.pop(list(sorted_dict)[0])
                b -= 1
        return list(sorted_dict.keys())
