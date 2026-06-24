# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: equalize-strings-by-adding-or-removing-characters-at-ends
# source_path: LeetCode-Solutions-master/Python/equalize-strings-by-adding-or-removing-characters-at-ends.py
# solution_class: Solution3
# submission_id: 281a96eee111f26aae8e357c6105f3169f665514
# seed: 4133598383

# Time:  O((n + m) * log(min(n, m)))
# Space: O(min(n, m))

# binary search, rolling hash

class Solution3(object):
    def minOperations(self, initial, target):
        """
        :type initial: str
        :type target: str
        :rtype: int
        """
        if len(initial) < len(target):
            initial, target = target, initial
        result = 0
        dp = [0]*(len(target)+1)
        for i in xrange(len(initial)):
            for j in reversed(xrange(len(target))):
                dp[j+1] = dp[j]+1 if initial[i] == target[j] else 0
            result = max(result, max(dp))
        return len(initial)+len(target)-2*result