# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: permutations-ii
# source_path: LeetCode-Solutions-master/Python/permutations-ii.py
# solution_class: Solution2
# submission_id: 7054835114dcd5f7395ace3b4186bdab40689690
# seed: 4181172356

# Time:  O(n * n!)
# Space: O(n)

class Solution2(object):
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        solutions = [[]]

        for num in nums:
            next = []
            for solution in solutions:
                for i in xrange(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)

            solutions = next

        return solutions