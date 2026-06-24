# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-sum-of-subsequence-powers
# source_path: LeetCode-Solutions-master/Python/find-the-sum-of-subsequence-powers.py
# solution_class: Solution2
# submission_id: 2457543ea908484a8a71fa095aa090102805abd1
# seed: 2636934628

# Time:  O(n^2 + len(diffs) * n * k) = O(n^3 * k) at most
# Space: O(len(diffs) + n * k) = O(n^2) at most

# sort, dp, prefix sum, two pointers

class Solution2(object):
    def sumOfPowers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        nums.sort()
        dp = [[collections.defaultdict(int) for _ in xrange(len(nums)+1)] for _ in xrange(len(nums))]        
        for i in xrange(len(nums)):
            for j in xrange(max(k-(len(nums)-i+1)-1, 0), i):
                diff = nums[i]-nums[j]
                dp[i][2][diff] += 1
                for l in xrange(max(k-(len(nums)-i+1), 0), i+1):
                    for mn, cnt in dp[j][l].iteritems():
                        dp[i][l+1][min(diff, mn)] = (dp[i][l+1][min(diff, mn)]+cnt)%MOD
        return reduce(lambda accu, x: (accu+x)%MOD, ((mn*cnt)%MOD for i in xrange(k-1, len(dp)) for mn, cnt in dp[i][k].iteritems()))