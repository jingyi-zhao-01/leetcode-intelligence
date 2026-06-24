# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: positions-of-large-groups
# source_path: LeetCode-Solutions-master/Python/positions-of-large-groups.py
# solution_class: Solution
# submission_id: a39d394e67e7e9e3964cd28c3e242c29ff4eb9ab
# seed: 2295113759

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        for j in xrange(len(S)):
            if j == len(S)-1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    result.append([i, j])
                i = j+1
        return result