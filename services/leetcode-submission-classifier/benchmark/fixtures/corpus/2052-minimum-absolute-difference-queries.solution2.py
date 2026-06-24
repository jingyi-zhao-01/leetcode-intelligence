# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-absolute-difference-queries
# source_path: LeetCode-Solutions-master/Python/minimum-absolute-difference-queries.py
# solution_class: Solution2
# submission_id: d37ba97423dadf04edab91a3972a007ccdc59150
# seed: 1149668101

# Time:  O(r * (n + q)), r is the max of nums
# Space: O(r * n)

class Solution2(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        INF = float("inf")
        idxs = [[] for _ in xrange(max(nums)+1)]
        for i, num in enumerate(nums):
            idxs[num].append(i)
        result = []
        for l, r in queries:
            min_diff, prev = INF, -1
            for num in xrange(len(idxs)):
                i = bisect.bisect_left(idxs[num], l)
                if not (i < len(idxs[num]) and idxs[num][i] <= r):
                    continue
                if prev != -1:
                    min_diff = min(min_diff, num-prev)
                prev = num
            result.append(min_diff if min_diff != INF else -1)
        return result