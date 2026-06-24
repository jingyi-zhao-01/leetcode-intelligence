# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-area-rectangle-with-point-constraints-i
# source_path: LeetCode-Solutions-master/Python/maximum-area-rectangle-with-point-constraints-i.py
# solution_class: Solution
# submission_id: 27cc5c2e297e544ee720c3b55ad76928aa61e95d
# seed: 3729014187

# Time:  O(nlogn)
# Space: O(n)

# sort, fenwick tree, hash table

class Solution(object):
    def maxRectangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        class BIT(object):  # 0-indexed.
            def __init__(self, n):
                self.__bit = [0]*(n+1)  # Extra one for dummy node.

            def add(self, i, val):
                i += 1  # Extra one for dummy node.
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += (i & -i)

            def query(self, i):
                i += 1  # Extra one for dummy node.
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret
    
        points.sort()
        y_to_idx = {y:idx for idx, y in enumerate(sorted(set(y for _, y in points)))}
        bit = BIT(len(y_to_idx))
        lookup = {}
        result = -1
        for i, (x, y) in enumerate(points):
            y_idx = y_to_idx[y]
            bit.add(y_idx, +1)
            if not (i-1 >= 0 and points[i-1][0] == x):
                continue
            prev_y_idx = y_to_idx[points[i-1][1]]
            curr = bit.query(y_idx)-bit.query(prev_y_idx-1)
            if (prev_y_idx, y_idx) in lookup and lookup[prev_y_idx, y_idx][0] == curr-2:
                result = max(result, (x-lookup[prev_y_idx, y_idx][1])*(y-points[i-1][1]))
            lookup[prev_y_idx, y_idx] = (curr, x)
        return result