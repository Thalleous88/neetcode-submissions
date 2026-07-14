class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        best = 0
        heights.append(0)
        for index, height in enumerate(heights):

            while stack and heights[stack[-1]] > height:
                temp = stack.pop()

                if stack:
                    width = index - stack[-1] - 1
                else:
                    width = index

                area = heights[temp] * width
            
                if area > best:
                    best = area
            
            stack.append(index)

        

        return best

            
