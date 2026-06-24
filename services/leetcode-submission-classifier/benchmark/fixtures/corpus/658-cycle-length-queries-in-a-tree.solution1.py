# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cycle-length-queries-in-a-tree
# source_path: LeetCode-Solutions-master/Python/cycle-length-queries-in-a-tree.py
# solution_class: Solution
# submission_id: b6e44ca4c69da5d58064d6a1699c0a1c6684b698
# seed: 3340166079

# Time:  O(q * n)
# Space: O(1)

# tree, lca

class Solution(object):
    def cycleLengthQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for x, y in queries:
            cnt = 1
            while x != y:
                if x > y:
                    x, y = y, x
                y //= 2
                cnt += 1
            result.append(cnt)
        return result