# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-get-a-peaceful-board
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-get-a-peaceful-board.py
# solution_class: Solution
# submission_id: 87d0aa5d152f5018d65e7cb0aae4e0ece25ddf8d
# seed: 87218538

# Time:  O(n)
# Space: O(n)

# counting sort, greedy

class Solution(object):
    def minMoves(self, rooks):
        """
        :type rooks: List[List[int]]
        :rtype: int
        """
        def count(arr):
            cnt = [0]*len(arr)
            for x in arr:
                cnt[x] += 1
            return sum(abs(i-x) for i, x in enumerate(x for x, cnt in enumerate(cnt) for _ in xrange(cnt)))

        return sum(count(arr) for arr in zip(*rooks))