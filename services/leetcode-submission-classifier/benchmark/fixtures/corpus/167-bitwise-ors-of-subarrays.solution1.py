# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-ors-of-subarrays
# source_path: LeetCode-Solutions-master/Python/bitwise-ors-of-subarrays.py
# solution_class: Solution
# submission_id: 74028f5022a7da32b7779f4795a5b932b3548c7e
# seed: 2773092973

# Time:  O(32 * n)
# Space: O(1)

class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, curr = set(), {0}
        for i in A:
            curr = {i} | {i | j for j in curr}
            result |= curr
        return len(result)