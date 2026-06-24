# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-white-tiles-covered-by-a-carpet
# source_path: LeetCode-Solutions-master/Python/maximum-white-tiles-covered-by-a-carpet.py
# solution_class: Solution2
# submission_id: 7c46e5f206b026daf1d2edd3431abfad528c8d5d
# seed: 857126435

# Time:  O(nlogn)
# Space: O(1)

# sliding window, optimized from solution3

class Solution2(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        tiles.sort()
        result = left = gap = 0
        for right in xrange(len(tiles)):
            if right-1 >= 0:
                gap += tiles[right][0]-tiles[right-1][1]-1
            l = tiles[right][1]-carpetLen+1
            while not (tiles[left][1]+1 >= l):
                left += 1
                gap -= tiles[left][0]-tiles[left-1][1]-1
            result = max(result, min(tiles[right][1]-tiles[left][0]+1, carpetLen)-gap)
        return result