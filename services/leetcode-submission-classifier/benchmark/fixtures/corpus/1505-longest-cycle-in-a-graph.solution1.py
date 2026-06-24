# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-cycle-in-a-graph
# source_path: LeetCode-Solutions-master/Python/longest-cycle-in-a-graph.py
# solution_class: Solution
# submission_id: fab67f8b5db4676d4def51950399b98dceb02d81
# seed: 318114390

# Time:  O(n)
# Space: O(n)

# graph

class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        result = -1
        lookup = [-1]*len(edges)
        idx = 0
        for i in xrange(len(edges)):
            if lookup[i] != -1:
                continue
            start = idx
            while i != -1:
                if lookup[i] != -1:
                    break
                lookup[i] = idx
                idx += 1
                i = edges[i]
            if i != -1 and lookup[i] >= start:
                result = max(result, idx-lookup[i])
        return result