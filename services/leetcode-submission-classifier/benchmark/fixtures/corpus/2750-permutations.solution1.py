# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutations
# source_path: LeetCode-Solutions-master/Python/permutations.py
# solution_class: Solution
# submission_id: 942e2333d4ad540ff0be6ef59be3088d95f42357
# seed: 3870004172

# Time:  O(n * n!)
# Space: O(n)

class Solution(object):
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.permuteRecu(result, used, [], num)
        return result

    def permuteRecu(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur[:])
            return
        for i in xrange(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRecu(result, used, cur, num)
                cur.pop()
                used[i] = False