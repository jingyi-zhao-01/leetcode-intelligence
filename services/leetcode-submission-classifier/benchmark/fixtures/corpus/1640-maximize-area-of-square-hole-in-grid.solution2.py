# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-area-of-square-hole-in-grid
# source_path: LeetCode-Solutions-master/Python/maximize-area-of-square-hole-in-grid.py
# solution_class: Solution2
# submission_id: bdea9b1e1737b3e4fb12c6896fe8fe84636d82f5
# seed: 644948203

# Time:  O(h + v), h = len(hBars), v = len(vBars)
# Space: O(h + v)

# array, hash table

class Solution2(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        def max_gap(arr):
            arr.sort()
            result = l = 1
            for i in xrange(len(arr)):
                l += 1
                result = max(result, l)
                if i+1 != len(arr) and arr[i+1] != arr[i]+1:
                    l = 1
            return result

        return min(max_gap(hBars), max_gap(vBars))**2