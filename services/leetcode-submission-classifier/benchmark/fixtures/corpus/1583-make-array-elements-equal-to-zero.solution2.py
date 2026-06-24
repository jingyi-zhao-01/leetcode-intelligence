# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-array-elements-equal-to-zero
# source_path: LeetCode-Solutions-master/Python/make-array-elements-equal-to-zero.py
# solution_class: Solution2
# submission_id: ad962a0985b2a53889e659e292648e42cb019a5d
# seed: 3170417036

# Time:  O(n)
# Space: O(1)

# prefix sum, CodeChef Starters 146 - Bouncing Ball (https://www.codechef.com/problems/BOUNCE_BALL)

class Solution2(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        suffix = [0]*(len(nums)+1)
        for i in reversed(xrange(len(nums))):
            suffix[i] = suffix[i+1]+nums[i]
        return sum(max(2-abs(prefix[i]-suffix[i+1]), 0) for i in xrange(len(nums)) if nums[i] == 0)