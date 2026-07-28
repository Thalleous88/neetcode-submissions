class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        

        lst = []

        def recursion(lst2, last_seen, lst):

            if len(lst2) == len(nums):
                lst.append(list(lst2))
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
                

                

            