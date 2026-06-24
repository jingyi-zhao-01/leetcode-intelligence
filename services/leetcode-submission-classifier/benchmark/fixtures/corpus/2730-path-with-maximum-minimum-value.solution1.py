# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-with-maximum-minimum-value
# source_path: LeetCode-Solutions-master/Python/path-with-maximum-minimum-value.py
# solution_class: Solution
# submission_id: fa1aa47115aae663ce0283c67c22302f9414504f
# seed: 867464208

# Time:  O(m * n * log(m * n))
# Space: O(m * n)

# binary search + dfs solution

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def check(A, val, r, c, lookup):
            if r == len(A)-1 and c == len(A[0])-1:
                return True
            lookup.add((r, c))
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < len(A) and \
                   0 <= nc < len(A[0]) and \
                   (nr, nc) not in lookup and \
                   A[nr][nc] >= val and \
                   check(A, val, nr, nc, lookup):
                    return True
            return False
        
        vals, ceil = [], min(A[0][0], A[-1][-1])
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if A[i][j] <= ceil:
                    vals.append(A[i][j])
        vals = list(set(vals))
        vals.sort()
        left, right = 0, len(vals)-1
        while left <= right:
            mid = left + (right-left)//2
            if not check(A, vals[mid], 0, 0, set()):
                right = mid-1
            else:
                left = mid+1
        return vals[right]