class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones = sorted(stones)
            y = stones[-1]-stones[-2]
            stones.remove(stones[-1])
            stones.remove(stones[-1])
            stones.append(y)
        return stones
