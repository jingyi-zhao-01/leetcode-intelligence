# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-number-of-elements-in-subset
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-number-of-elements-in-subset.py
# solution_class: Solution2
# submission_id: 58ba2b91188de8ff95ffacca305f2bcdabb34d30
# seed: 2939484113

# Time:  O(n)
# Space: O(n)

import collections


# freq table, dp

class Solution2(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        result = 0
        for x in cnt.iterkeys():
            if x == 1:
                result = max(result, cnt[x]-(1 if cnt[x]%2 == 0 else 0))
                continue
            l = 0
            while x in cnt and cnt[x] >= 2:
                l += 2
                x *= x
            l += 1 if x in cnt else -1
            result = max(result, l)
        return result 