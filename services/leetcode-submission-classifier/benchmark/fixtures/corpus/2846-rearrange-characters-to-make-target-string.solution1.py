# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-characters-to-make-target-string
# source_path: LeetCode-Solutions-master/Python/rearrange-characters-to-make-target-string.py
# solution_class: Solution
# submission_id: e6662d5e1fb99b44e529cdfa448689cc6340ab09
# seed: 1365432082

# Time:  O(n + m)
# Space: O(1)

import collections


# freq table

class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        cnt1 = collections.Counter(s)
        cnt2 = collections.Counter(target)
        return min(cnt1[k]//v for k, v in cnt2.iteritems())