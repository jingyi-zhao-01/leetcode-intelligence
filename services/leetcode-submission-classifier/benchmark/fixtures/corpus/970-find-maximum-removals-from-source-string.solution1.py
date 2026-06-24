# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-removals-from-source-string
# source_path: LeetCode-Solutions-master/Python/find-maximum-removals-from-source-string.py
# solution_class: Solution
# submission_id: fa9fbe54a4b15e64b4b4092b677c7146e0599b7b
# seed: 2893523518

# Time:  O(n * m)
# Space: O(n + m)

# dp

class Solution(object):
    def maxRemovals(self, source, pattern, targetIndices):
        """
        :type source: str
        :type pattern: str
        :type targetIndices: List[int]
        :rtype: int
        """
        dp = [float("-inf")]*(len(pattern)+1)
        dp[0] = 0
        lookup = [False]*len(source)
        for x in targetIndices:
            lookup[x] = True
        for i in xrange(len(source)):
            for j in reversed(xrange(len(pattern)+1)):
                dp[j] += lookup[i]
                if j-1 >= 0 and pattern[j-1] == source[i]:
                    dp[j] = max(dp[j], dp[j-1])
        return dp[-1]