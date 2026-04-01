class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        res = 0

        while L != R:
            area = ((R - L) * min(heights[R], heights[L]))
            res = max(area, res)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L +=1
        return res

        