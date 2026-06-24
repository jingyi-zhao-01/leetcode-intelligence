# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-white-tiles-covered-by-a-carpet
# source_path: LeetCode-Solutions-master/Python/maximum-white-tiles-covered-by-a-carpet.py
# solution_class: Solution4
# submission_id: c4a98ee536948f4ce3db43acc6af45a945b6bd2f
# seed: 3025936678

# Time:  O(nlogn)
# Space: O(1)

# sliding window, optimized from solution3

class Solution4(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        tiles.sort()
        prefix = [0]*(len(tiles)+1)
        for i, (l, r) in enumerate(tiles):
            prefix[i+1] = prefix[i]+(r-l+1)
        result = 0
        for right, (_, r) in enumerate(tiles):
            l = r-carpetLen+1
            left = bisect.bisect_right(tiles, [l])
            if left-1 >= 0 and tiles[left-1][1]+1 >= l:
                left -= 1
            extra = max(l-tiles[left][0], 0)
            result = max(result, (prefix[right+1]-prefix[left])-extra)
        return result