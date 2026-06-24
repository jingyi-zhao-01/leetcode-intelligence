# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-and-sum-of-array
# source_path: LeetCode-Solutions-master/Python/maximum-and-sum-of-array.py
# solution_class: Solution3
# submission_id: 5735ef4180ae214df88153926fe1960e3c37e602
# seed: 3435788373

# Time:  O(n^3)
# Space: O(n^2)

# weighted bipartite matching solution

class Solution3(object):
    def maximumANDSum(self, nums, numSlots):
        """
        :type nums: List[int]
        :type numSlots: int
        :rtype: int
        """
        def count(x):
            result = 0
            while x:
                result += x%3
                x //= 3
            return result

        dp = [0]*(3**numSlots)
        for mask in xrange(1, len(dp)):
            i = count(mask)-1
            x = nums[i] if i < len(nums) else 0
            base = 1
            for slot in xrange(1, numSlots+1):
                if mask//base%3:
                    dp[mask] = max(dp[mask], (x&slot)+dp[mask-base])
                base *= 3
        return dp[-1]