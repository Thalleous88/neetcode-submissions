class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        t = [len(nums)-i for i in range(len(nums))]
        total = 1
        for n in t:
            total *= n
        print(total)

        lst = []

        def recursion(lst2, last_seen, lst):

            if len(lst2) == len(nums):
                lst.append(list(lst2))
                return
            if len(lst) >= total:
                return

            for num in nums:
                if num in last_seen:
                    continue

                lst2.append(num)
                last_seen.add(num)

                recursion(lst2, last_seen, lst)

                last_seen.remove(num)

                lst2.pop()

        recursion([], set(), lst)

        return lst
                

                

            