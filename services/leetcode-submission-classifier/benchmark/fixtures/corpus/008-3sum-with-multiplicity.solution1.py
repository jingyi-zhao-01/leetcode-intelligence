# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 3sum-with-multiplicity
# source_path: LeetCode-Solutions-master/Python/3sum-with-multiplicity.py
# solution_class: Solution
# submission_id: c61c765f9f41292163eb01e3e083951c27cc4f64
# seed: 1503117443

# Time:  O(n^2), n is the number of disctinct A[i]
# Space: O(n)

import collections
import itertools

class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        count = collections.Counter(A)
        result = 0
        for i, j in itertools.combinations_with_replacement(count, 2):
            k = target - i - j
            if i == j == k:
                result += count[i] * (count[i]-1) * (count[i]-2) // 6
            elif i == j != k:
                result += count[i] * (count[i]-1) // 2 * count[k]
            elif max(i, j) < k:
                result += count[i] * count[j] * count[k]
        return result % (10**9 + 7)