# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-the-xor-of-all-segments-equal-to-zero
# source_path: LeetCode-Solutions-master/Python/make-the-xor-of-all-segments-equal-to-zero.py
# solution_class: Solution
# submission_id: b57e1e20345bae861ce2a86e717bbc0a7323456e
# seed: 2185278431

# Time:  O(n + k * m), m is the max number of nums
# Space: O(min(k * m, n))

import collections

class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def one_are_not_from_nums(nums, cnts):
            mxs = [cnts[i].most_common(1)[0][1] for i in xrange(k)]
            return len(nums) - (sum(mxs)-min(mxs))

        def all_are_from_nums(nums, cnts):
            dp = {0:0}
            for cnt in cnts:
                new_dp = collections.defaultdict(int)
                for x in dp.iterkeys():
                    for y in cnt.iterkeys():
                        new_dp[x^y] = max(new_dp[x^y], dp[x]+cnt[y])
                dp = new_dp
            return len(nums)-dp[0]
          
        cnts = [collections.Counter(nums[j] for j in xrange(i, len(nums), k)) for i in xrange(k)]
        return min(one_are_not_from_nums(nums, cnts), all_are_from_nums(nums, cnts))