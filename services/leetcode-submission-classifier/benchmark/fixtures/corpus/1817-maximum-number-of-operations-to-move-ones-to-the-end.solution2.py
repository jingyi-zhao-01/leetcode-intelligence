# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-operations-to-move-ones-to-the-end
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-operations-to-move-ones-to-the-end.py
# solution_class: Solution2
# submission_id: e0358040484623bf805e9249f20aa7d3acc92900
# seed: 508700613

# Time:  O(n)
# Space: O(1)

# greedy

class Solution2(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = curr = 0
        for i in xrange(len(s)):
            if s[i] != '1':
                continue
            curr += 1
            if i+1 < len(s) and s[i+1] == '0':
                result += curr
        return result