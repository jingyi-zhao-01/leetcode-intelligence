# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-of-a-good-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-score-of-a-good-subarray.py
# solution_class: Solution2
# submission_id: af2259b2daf62588cdb18b2e5d4fa1cf8f964542
# seed: 3291292792

# Time:  O(n)
# Space: O(n)

class Solution2(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def score(nums, k):
            prefix = [nums[k]]*(k+1)
            for i in reversed(xrange(k)):
                prefix[i] = min(prefix[i+1], nums[i])
            result = right = nums[k]
            for j in xrange(k+1, len(nums)):
                right = min(right, nums[j])
                i = bisect.bisect_left(prefix, right)
                if i >= 0:
                    result = max(result, right*(j-i+1))
            return result

        return max(score(nums, k), score(nums[::-1], len(nums)-1-k))