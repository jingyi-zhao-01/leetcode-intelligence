# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: combination-sum-iii
# source_path: LeetCode-Solutions-master/Python/combination-sum-iii.py
# solution_class: Solution
# submission_id: 966058138b255b5228b821dd2db95ec257c19424
# seed: 128566517

# Time:  O(k * C(n, k))
# Space: O(k)

class Solution(object):
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        result = []
        self.combinationSumRecu(result, [], 1, k, n)
        return result

    def combinationSumRecu(self, result, intermediate, start, k, target):
        if k == 0 and target == 0:
            result.append(list(intermediate))
        elif k < 0:
            return
        while start < 10 and start * k + k * (k - 1) / 2 <= target:
            intermediate.append(start)
            self.combinationSumRecu(result, intermediate, start + 1, k - 1, target - start)
            intermediate.pop()
            start += 1