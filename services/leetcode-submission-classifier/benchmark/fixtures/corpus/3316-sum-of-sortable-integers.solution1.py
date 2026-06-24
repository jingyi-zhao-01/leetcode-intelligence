# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-sortable-integers
# source_path: LeetCode-Solutions-master/Python/sum-of-sortable-integers.py
# solution_class: Solution
# submission_id: d9af9b8369cc7541167e37f3118f0f6870328a64
# seed: 2272148199

# Time:  O(nlog(logn))
# Space: O(n)

# prefix sum, number theory

class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(k):
            return len(nums)%k == 0 and all(prefix[i] <= suffix[i] and (prefix2[i+k-1]-prefix2[i])+(1 if nums[i+k-1] > nums[i] else 0) <= 1 for i in xrange(0, len(nums), k))

        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = max(prefix[i], nums[i])
        suffix = [float("inf")]*(len(nums)+1)
        for i in reversed(xrange(len(nums))):
            suffix[i] = min(suffix[i+1], nums[i])
        prefix2 = [0]*(len(nums))
        for i in xrange(len(nums)-1):
            prefix2[i+1] = prefix2[i]+(1 if nums[i] > nums[i+1] else 0)
        return sum(k for k in xrange(1, len(nums)+1) if check(k))