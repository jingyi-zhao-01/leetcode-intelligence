# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-original-array-of-prefix-xor
# source_path: LeetCode-Solutions-master/Python/find-the-original-array-of-prefix-xor.py
# solution_class: Solution
# submission_id: 61afad85854675a2133435b16cf60509644ae2c5
# seed: 762963554

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        for i in reversed(xrange(1, len(pref))):
            pref[i] ^= pref[i-1]
        return pref