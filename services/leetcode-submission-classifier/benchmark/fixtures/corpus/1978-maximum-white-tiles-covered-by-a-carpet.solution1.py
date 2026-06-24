# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-white-tiles-covered-by-a-carpet
# source_path: LeetCode-Solutions-master/Python/maximum-white-tiles-covered-by-a-carpet.py
# solution_class: Solution
# submission_id: 3edbf5ae57ae23c5ce77bb7ca126fd19debde3eb
# seed: 2389222787

# Time:  O(nlogn)
# Space: O(1)

# sliding window, optimized from solution3

class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        tiles.sort()
        result = right = gap = 0
        for left, (l, _) in enumerate(tiles):
            if left-1 >= 0:
                gap -= tiles[left][0]-tiles[left-1][1]-1
            r = l+carpetLen-1
            while right+1 < len(tiles) and r+1 >= tiles[right+1][0]:
                right += 1
                gap += tiles[right][0]-tiles[right-1][1]-1
            result = max(result, min(tiles[right][1]-tiles[left][0]+1, carpetLen)-gap)
        return result