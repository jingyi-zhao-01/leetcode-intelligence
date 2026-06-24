# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-reach-destination-in-the-grid
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-reach-destination-in-the-grid.py
# solution_class: Solution2
# submission_id: 0d61689653f99253d3b584836a8c1148e1f1cd87
# seed: 2763450034

# Time:  O(logn)
# Space: O(1)

# dp, matrix exponentiation

class Solution2(object):
    def numberOfWays(self, n, m, k, source, dest):
        """
        :type n: int
        :type m: int
        :type k: int
        :type source: List[int]
        :type dest: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        both_same = row_same = col_same = no_same = 0
        if source == dest:
            both_same = 1
        elif source[0] == dest[0]:
            row_same = 1
        elif source[1] == dest[1]:
            col_same = 1
        else:
            no_same = 1
        for _ in xrange(k):
            both_same, row_same, col_same, no_same = (row_same+col_same)%MOD, (both_same*(m-1)+row_same*(m-2)+no_same)%MOD, (both_same*(n-1)+col_same*(n-2)+no_same)%MOD, (row_same*(n-1)+col_same*(m-1)+no_same*((n-2)+(m-2)))%MOD
        return both_same