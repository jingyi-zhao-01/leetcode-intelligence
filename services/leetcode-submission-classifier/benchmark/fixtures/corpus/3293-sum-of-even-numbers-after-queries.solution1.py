# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-even-numbers-after-queries
# source_path: LeetCode-Solutions-master/Python/sum-of-even-numbers-after-queries.py
# solution_class: Solution
# submission_id: b2483d64580c2b0793e93b8716250d99106f25fe
# seed: 3625641408

# Time:  O(n + q)
# Space: O(1)

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total = sum(v for v in A if v % 2 == 0)
        
        result = []
        for v, i in queries:
            if A[i] % 2 == 0:
                total -= A[i]
            A[i] += v
            if A[i] % 2 == 0:
                total += A[i]
            result.append(total)
        return result