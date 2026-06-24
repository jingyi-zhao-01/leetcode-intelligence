# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-special-subsequences
# source_path: LeetCode-Solutions-master/Python/count-special-subsequences.py
# solution_class: Solution2
# submission_id: a614b140bb0498ddb3ca96e2667eebcad0c4ebd0
# seed: 1771637165

# Time:  O(n^2)
# Space: O(n^2)

import collections


# freq table

class Solution2(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
    
        cnt = collections.defaultdict(int)
        result = 0
        for r in xrange(4, len(nums)-2):
            q = r-2
            for p in xrange((q-2)+1):
                g = gcd(nums[p], nums[q])
                cnt[nums[p]//g, nums[q]//g] += 1
            for s in xrange(r+2, len(nums)):
                g = gcd(nums[s], nums[r])
                result += cnt[nums[s]//g, nums[r]//g]
        return result