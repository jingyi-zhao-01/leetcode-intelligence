# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-value-sum-by-placing-three-rooks-i
# source_path: LeetCode-Solutions-master/Python/maximum-value-sum-by-placing-three-rooks-i.py
# solution_class: Solution2
# submission_id: f43aa93ff6e9c77a08539c1a603060f32e44fa6a
# seed: 1745676986

# Time:  O(m * n * logk + nCr((k-1)*(2*k-1)+1), k) * k) = O(m * n)
# Space: O(k * (m + n)) = O(m + n)

import heapq
import itertools


# heap, brute force

class Solution2(object):
    def maximumValueSum(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        k = 3
        rows = [heapq.nlargest(k, [(board[i][j], i, j) for j in xrange(len(board[0]))]) for i in xrange(len(board))]
        cols = [heapq.nlargest(k, [(board[i][j], i, j) for i in xrange(len(board))]) for j in xrange(len(board[0]))]
        min_heap = heapq.nlargest((k-1)*(2*k-1)+1, set(itertools.chain(*rows)) & set(itertools.chain(*cols)))  # each choice excludes at most 2k-1 candidates, we should have at least (k-1)*(2k-1)+1 candidates
        return max(sum(x[0] for x in c) for c in itertools.combinations(min_heap, k) if len({x[1] for x in c}) == k == len({x[2] for x in c}))