# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: get-maximum-in-generated-array
# source_path: LeetCode-Solutions-master/Python/get-maximum-in-generated-array.py
# solution_class: Solution2
# submission_id: 558927a42cbbb9c2f18873fcbf8a898ba076c473
# seed: 4270534696

# Time:  O(n)
# Space: O(n)

nums = [0, 1]
dp = [0, 1]

class Solution2(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        nums = [0]*(n+1)
        nums[1] = 1
        result = 1
        for i in xrange(2, n+1):
            if i%2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2+1]
            result = max(result, nums[i])
        return result