# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-or-of-all-subsequence-sums
# source_path: LeetCode-Solutions-master/Python/bitwise-or-of-all-subsequence-sums.py
# solution_class: Solution2
# submission_id: 4f7aad0269c4214ace804c5f3cd3a5295a72ff15
# seed: 2219487164

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution2(object):
    def subsequenceSumOr(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = cnt = 0
        for i in xrange(64):
            cnt >>= 1
            for x in nums:
                cnt += (x>>i)&1
            if cnt:
                result |= 1<<i
        return result