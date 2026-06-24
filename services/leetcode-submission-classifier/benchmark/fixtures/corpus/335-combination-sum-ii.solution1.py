# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: combination-sum-ii
# source_path: LeetCode-Solutions-master/Python/combination-sum-ii.py
# solution_class: Solution
# submission_id: c5003b7929d050afad2b444234ffefc7fdd44dab
# seed: 267217867

# Time:  O(k * C(n, k))
# Space: O(k)

class Solution(object):
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if prev != candidates[start]:
                intermediate.append(candidates[start])
                self.combinationSumRecu(candidates, result, start + 1, intermediate, target - candidates[start])
                intermediate.pop()
                prev = candidates[start]
            start += 1