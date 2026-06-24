# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: form-largest-integer-with-digits-that-add-up-to-target
# source_path: LeetCode-Solutions-master/Python/form-largest-integer-with-digits-that-add-up-to-target.py
# solution_class: Solution3
# submission_id: e77f84a4b43493c532f526b8297500e2c63804ee
# seed: 775303481

# Time:  O(t)
# Space: O(t)

class Solution3(object):
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
                if t-c < 0:
                    continue
                dp[t] = max(dp[t], dp[t-c]*10 + i+1)
        return str(max(dp[t], 0))