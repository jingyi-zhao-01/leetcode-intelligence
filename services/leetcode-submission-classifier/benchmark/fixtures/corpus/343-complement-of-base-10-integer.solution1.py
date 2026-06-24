# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: complement-of-base-10-integer
# source_path: LeetCode-Solutions-master/Python/complement-of-base-10-integer.py
# solution_class: Solution
# submission_id: 8d7ecf127ea9552d31219183b645d0bb1af6f856
# seed: 1877601740

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        mask = 1
        while N > mask:
            mask = mask*2+1
        return mask-N