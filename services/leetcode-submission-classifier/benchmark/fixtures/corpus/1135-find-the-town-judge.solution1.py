# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-town-judge
# source_path: LeetCode-Solutions-master/Python/find-the-town-judge.py
# solution_class: Solution
# submission_id: fd460a5a7258ab080a62904ed0cab5cfeb4d8285
# seed: 2137946900

# Time:  O(t + n)
# Space: O(n)

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        degrees = [0]*N
        for i, j in trust:
            degrees[i-1] -= 1
            degrees[j-1] += 1
        for i in xrange(len(degrees)):
            if degrees[i] == N-1:
                return i+1
        return -1