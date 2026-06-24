# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-happiness-of-selected-children
# source_path: LeetCode-Solutions-master/Python/maximize-happiness-of-selected-children.py
# solution_class: Solution
# submission_id: 745ecdb0d4565ff21b2e5cd0d37e4358a202c9b0
# seed: 3741355958

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        return sum(max(happiness[i]-i, 0) for i in xrange(k))