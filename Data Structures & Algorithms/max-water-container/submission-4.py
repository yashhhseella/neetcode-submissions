class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L, R = 0, len(heights) - 1

        volume = 0

        while L < R:
            currentArea = (R - L) * min(heights[L], heights[R])
            volume = max(volume, currentArea)
            if heights[R] < heights[L]:
                R -= 1
            else:
                L += 1
        
        return volume

        