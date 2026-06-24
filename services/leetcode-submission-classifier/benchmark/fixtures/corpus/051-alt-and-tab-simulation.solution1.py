# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: alt-and-tab-simulation
# source_path: LeetCode-Solutions-master/Python/alt-and-tab-simulation.py
# solution_class: Solution
# submission_id: 09d259a533d29d2e8b15bb9c052e216db984ab97
# seed: 3688844485

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def simulationResult(self, windows, queries):
        """
        :type windows: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        lookup = [False]*len(windows)
        result = []
        for x in reversed(queries):
            if lookup[x-1]:
                continue
            lookup[x-1] = True
            result.append(x)
        result.extend(x for x in windows if not lookup[x-1])
        return result