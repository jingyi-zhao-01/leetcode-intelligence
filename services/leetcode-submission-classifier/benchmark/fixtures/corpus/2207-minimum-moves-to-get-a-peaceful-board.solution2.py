# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-get-a-peaceful-board
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-get-a-peaceful-board.py
# solution_class: Solution2
# submission_id: c298ac9f349c17d25405fd0c984b62f6e71d826f
# seed: 3606537193

# Time:  O(n)
# Space: O(n)

# counting sort, greedy

class Solution2(object):
    def minMoves(self, rooks):
        """
        :type rooks: List[List[int]]
        :rtype: int
        """
        def count(arr):
            cnt = [0]*len(arr)
            for x in arr:
                cnt[x] += 1
            result = bal = 0
            for i in xrange(len(rooks)):
                bal += cnt[i]-1
                result += abs(bal)
            return result

        return sum(count(arr) for arr in zip(*rooks))