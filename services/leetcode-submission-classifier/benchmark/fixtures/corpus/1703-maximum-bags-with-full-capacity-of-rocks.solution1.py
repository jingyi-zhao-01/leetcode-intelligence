# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-bags-with-full-capacity-of-rocks
# source_path: LeetCode-Solutions-master/Python/maximum-bags-with-full-capacity-of-rocks.py
# solution_class: Solution
# submission_id: 4567b5760659ef04722e7437d62b93e4e884798b
# seed: 2632933809

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        for i in xrange(len(capacity)):
            capacity[i] -= rocks[i]
        capacity.sort()
        for i, c in enumerate(capacity):
            if c > additionalRocks:
                return i
            additionalRocks -= c
        return len(capacity)