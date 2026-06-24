# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: form-largest-integer-with-digits-that-add-up-to-target
# source_path: LeetCode-Solutions-master/Python/form-largest-integer-with-digits-that-add-up-to-target.py
# solution_class: Solution
# submission_id: 2d9094be776a463b9908c91923dc7431aab924fe
# seed: 3250908443

# Time:  O(t)
# Space: O(t)

class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [0]
        for t in xrange(1, target+1):
            dp.append(-1)
            for i, c in enumerate(cost):
                if t-c < 0 or dp[t-c] < 0:
                    continue
                dp[t] = max(dp[t], dp[t-c]+1)
        if dp[target] < 0:
            return "0"
        result = []
        for i in reversed(xrange(9)):
            while target >= cost[i] and dp[target] == dp[target-cost[i]]+1:
                target -= cost[i]
                result.append(i+1)
        return "".join(map(str, result))