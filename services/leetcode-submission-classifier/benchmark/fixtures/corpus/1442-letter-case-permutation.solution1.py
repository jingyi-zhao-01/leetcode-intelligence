# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: letter-case-permutation
# source_path: LeetCode-Solutions-master/Python/letter-case-permutation.py
# solution_class: Solution
# submission_id: e1b62abd206df54842fea5362b6a67891386f79f
# seed: 2520044653

# Time:  O(n * 2^n)
# Space: O(n * 2^n)

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = [[]]
        for c in S:
            if c.isalpha():
                for i in xrange(len(result)):
                    result.append(result[i][:])
                    result[i].append(c.lower())
                    result[-1].append(c.upper())
            else:
                for s in result:
                    s.append(c)
        return map("".join, result)