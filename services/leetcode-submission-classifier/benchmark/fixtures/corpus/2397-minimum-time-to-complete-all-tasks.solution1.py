# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-complete-all-tasks
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-complete-all-tasks.py
# solution_class: Solution
# submission_id: bd1df1d3f7307fb61b7d80a6d52270d7565878f7
# seed: 956486720

# Time:  O(nlogn + n * r), r = max(e for _, e in tasks)
# Space: O(r)

# sort, greedy

class Solution(object):
    def findMinimumTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[1])
        lookup = set()
        for s, e, d in tasks:
            d -= sum(i in lookup for i in xrange(s, e+1))
            for i in reversed(xrange(1, e+1)):
                if d <= 0:
                    break
                if i in lookup:
                    continue
                lookup.add(i)
                d -= 1
        return len(lookup)