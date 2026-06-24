# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-white-tiles-covered-by-a-carpet
# source_path: LeetCode-Solutions-master/Python/maximum-white-tiles-covered-by-a-carpet.py
# solution_class: Solution3
# submission_id: 3df7f6152e505bb8eaae547ddbdcbf8b360ceaf2
# seed: 2827401908

# Time:  O(nlogn)
# Space: O(1)

# sliding window, optimized from solution3

class Solution3(object):
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
        for left, (l, _) in enumerate(tiles):
            r = l+carpetLen-1
            right = bisect.bisect_right(tiles, [r+1])-1
            extra = max(tiles[right][1]-r, 0)
            result = max(result, (prefix[right+1]-prefix[left])-extra)
        return result