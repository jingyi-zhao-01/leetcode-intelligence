# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: calculate-digit-sum-of-a-string
# source_path: LeetCode-Solutions-master/Python/calculate-digit-sum-of-a-string.py
# solution_class: Solution
# submission_id: faedbb5e9c66e3645644b76318d5fc21bd93b0c9
# seed: 1638721923

# Time:  O(n + n * (log10(9k)/k) + ... + k)
#      = O((n - (log10(9k)/k)*k)/(1-log10(9k)/k))
#      = O(n / (1-log10(9k)/k)) = O(n) for k >= 2
# Space: O(n)

# simulation

class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            s = "".join(map(str, (sum(map(int, s[i:i+k])) for i in xrange(0, len(s), k))))
        return s