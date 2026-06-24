# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-importance-of-roads
# source_path: LeetCode-Solutions-master/Python/maximum-total-importance-of-roads.py
# solution_class: Solution2
# submission_id: 7c687ab4d71e941eb3d807eb0571fcf8ec5afaab
# seed: 3016534938

# Time:  O(n)
# Space: O(n)

# greedy, counting sort

class Solution2(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0]*n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        return sum(i*x for i, x in enumerate(degree, 1))