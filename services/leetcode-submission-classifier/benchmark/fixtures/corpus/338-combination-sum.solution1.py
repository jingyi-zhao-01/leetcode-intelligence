# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: combination-sum
# source_path: LeetCode-Solutions-master/Python/combination-sum.py
# solution_class: Solution
# submission_id: b02e3052f1198c6756b0de31bb16b2107e629216
# seed: 1266116193

# Time:  O(k * n^k)
# Space: O(k)

class Solution(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            self.combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1