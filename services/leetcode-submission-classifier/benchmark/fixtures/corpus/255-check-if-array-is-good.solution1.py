# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-array-is-good
# source_path: LeetCode-Solutions-master/Python/check-if-array-is-good.py
# solution_class: Solution
# submission_id: 951a221d127663ab29e920ce9bd3f1294eeeea77
# seed: 699484059

# Time:  O(n)
# Space: O(n)

# freq table

class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = [0]*len(nums)
        for x in nums:
            if x < len(cnt):
                cnt[x] += 1
            else:
                return False
        return all(cnt[x] == 1 for x in xrange(1, len(nums)-1))