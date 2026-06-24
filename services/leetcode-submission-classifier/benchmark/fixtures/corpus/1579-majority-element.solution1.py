# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: majority-element
# source_path: LeetCode-Solutions-master/Python/majority-element.py
# solution_class: Solution
# submission_id: 52ce2e7bf92e9a467937241ed6b4f1ec60bb1992
# seed: 1878868706

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def boyer_moore_majority_vote():
            result, cnt = None, 0
            for x in nums:
                if not cnt:
                    result = x
                if x == result:
                    cnt += 1
                else:
                    cnt -= 1
            return result

        return boyer_moore_majority_vote()