# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-center-of-star-graph
# source_path: LeetCode-Solutions-master/Python/find-center-of-star-graph.py
# solution_class: Solution
# submission_id: b704b38304990039971370a46afbb00f884f249e
# seed: 3582007543

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        return edges[0][edges[0][1] in edges[1]]