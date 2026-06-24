# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-into-three-parts-with-equal-sum
# source_path: LeetCode-Solutions-master/Python/partition-array-into-three-parts-with-equal-sum.py
# solution_class: Solution
# submission_id: 90635490906152e4aa7583c44629e3a8f5358357
# seed: 1338347010

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = sum(A)
        if total % 3 != 0:
            return False
        parts, curr = 0, 0
        for x in A:
            curr += x
            if curr == total//3:
                parts += 1
                curr = 0
        return parts >= 3