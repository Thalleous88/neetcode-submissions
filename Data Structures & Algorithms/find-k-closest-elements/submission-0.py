class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0

        l = len(arr) - k + 1

        curr = []
        minn = float('inf')

        for i in range(l):
            temp = arr[i:i+k]
            temp = [e - x for e in temp]
            temp = sum([e * -1 if e < 0 else e for e in temp])

            print(temp)

            if minn > temp:
                minn = temp
                curr = arr[i:i+k]

        return curr


        
                