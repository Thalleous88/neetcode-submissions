class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        l = len(nums)
        lst = []

        lst.append([])
        

        def recursion(lst2, index, nums, lst):
            if index > l - 1:
                return


            for x in range(index, l):
                lst2.append(nums[x])
                
                lst.append(list(lst2))
                recursion(lst2, x+1, nums, lst)

                lst2.pop()


            
            

        recursion([], 0, nums, lst)
            
        return lst

        