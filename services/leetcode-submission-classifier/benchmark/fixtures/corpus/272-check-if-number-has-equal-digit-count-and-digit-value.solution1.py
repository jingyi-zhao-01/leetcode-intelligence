# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-number-has-equal-digit-count-and-digit-value
# source_path: LeetCode-Solutions-master/Python/check-if-number-has-equal-digit-count-and-digit-value.py
# solution_class: Solution
# submission_id: 755db98bc0879fe177132579f75150ad9cfd5c20
# seed: 413521987

# Time:  O(n)
# Space: O(1)

import collections


# freq table

class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        cnt = collections.Counter(num)
        return all(cnt[str(i)] == int(x) for i, x in enumerate(num))