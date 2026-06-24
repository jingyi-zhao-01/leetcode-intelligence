# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: combinations
# source_path: LeetCode-Solutions-master/Python/combinations.py
# solution_class: Solution2
# submission_id: acff6f27b62abd3adeba339f187940dcc7d7ee1a
# seed: 1029029649

# Time:  O(k * C(n, k))
# Space: O(k)

class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result, combination = [], []
        i = 1
        while True:
            if len(combination) == k:
                result.append(combination[:])
            if len(combination) == k or \
               len(combination)+(n-i+1) < k:
                if not combination:
                    break
                i = combination.pop()+1
            else:
                combination.append(i)
                i += 1
        return result