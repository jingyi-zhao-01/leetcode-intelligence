# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: get-maximum-in-generated-array
# source_path: LeetCode-Solutions-master/Python/get-maximum-in-generated-array.py
# solution_class: Solution
# submission_id: 796809387db6ed52c29af42c3daedea0604bb3f0
# seed: 1701792857

# Time:  O(n)
# Space: O(n)

nums = [0, 1]
dp = [0, 1]

class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n+1 > len(dp):
            for i in xrange(len(nums), n+1):
                if i%2 == 0:
                    nums.append(nums[i//2])
                else:
                    nums.append(nums[i//2] + nums[i//2+1])
                dp.append(max(dp[-1], nums[-1]))
        return dp[n]