class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = [0, 0, 0]
        for triplet in triplets:
            a, b, c = max(check[0], triplet[0]), max(check[1], triplet[1]), max(check[2], triplet[2])

            if a > target[0] or b > target[1] or c > target[2]:
                continue

            check[0], check[1], check[2] = a, b, c

        
        if check == target:
            return True

        return False


