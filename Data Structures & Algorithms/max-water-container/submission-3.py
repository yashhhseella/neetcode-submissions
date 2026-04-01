class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(length, h):
            return length * h


        L, R = 0, len(heights) - 1
        gallons = 0

        while L < R:
            height = min(heights[R], heights[L])
            
            currWater = area((R-L), height)
            gallons = max(gallons, currWater)

            if heights[R] < heights[L]:
                R-=1
            else:
                L+=1
        return gallons
