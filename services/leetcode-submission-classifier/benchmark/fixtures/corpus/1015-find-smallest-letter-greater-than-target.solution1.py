# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-smallest-letter-greater-than-target
# source_path: LeetCode-Solutions-master/Python/find-smallest-letter-greater-than-target.py
# solution_class: Solution
# submission_id: 97c27cbad37a1c3158bf050c08b2fd6d7e7df81c
# seed: 54920595

# Time:  O(logn)
# Space: O(1)

import bisect

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        i = bisect.bisect_right(letters, target)
        return letters[0] if i == len(letters) else letters[i]