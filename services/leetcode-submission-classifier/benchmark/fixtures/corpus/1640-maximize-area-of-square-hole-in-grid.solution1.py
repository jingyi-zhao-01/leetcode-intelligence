# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-area-of-square-hole-in-grid
# source_path: LeetCode-Solutions-master/Python/maximize-area-of-square-hole-in-grid.py
# solution_class: Solution
# submission_id: 35bbd82806e4b06515aaea4dc2bc15310e38305b
# seed: 3194544811

# Time:  O(h + v), h = len(hBars), v = len(vBars)
# Space: O(h + v)

# array, hash table

class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        def max_gap(arr):
            result = l = 1
            lookup = set(arr)
            while lookup:
                x = next(iter(lookup))
                left = x
                while left-1 in lookup:
                    left -= 1
                right = x
                while right+1 in lookup:
                    right += 1
                for i in xrange(left, right+1):
                    lookup.remove(i)
                result = max(result, (right-left+1)+1)
            return result

        return min(max_gap(hBars), max_gap(vBars))**2