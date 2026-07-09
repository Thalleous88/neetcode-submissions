class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        arr = [i for m in matrix for i in m]
        size = len(arr) - 1

        def bisearch(arr, target, left, right):
            if (right >= left):
                mid = left + (right-left)//2

                if (arr[mid] == target):
                    return True
                elif (arr[mid] > target):
                    return bisearch(arr, target, left, mid-1)
                else:
                    return bisearch(arr, target, mid+1, right)

            else:
                return False


        res = bool(bisearch(arr, target, 0, size))

        return res