# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: global-and-local-inversions
# source_path: LeetCode-Solutions-master/Python/global-and-local-inversions.py
# solution_class: Solution
# submission_id: 82039e63ac51099c5287d33dec0261458f257d03
# seed: 2185131666

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(abs(v-i) <= 1 for i,v in enumerate(A))