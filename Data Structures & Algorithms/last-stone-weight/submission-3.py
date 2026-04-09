class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)
        # this makes every element in the list negative
        # can also be done by * -1 for i in list

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, x - y)
            
        stones.append(0)

        return stones[0] * -1
        