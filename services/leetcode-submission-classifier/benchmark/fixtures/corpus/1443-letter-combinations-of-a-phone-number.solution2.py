# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: letter-combinations-of-a-phone-number
# source_path: LeetCode-Solutions-master/Python/letter-combinations-of-a-phone-number.py
# solution_class: Solution2
# submission_id: 724129dfa970c4532c207db35d6827e94d1f652b
# seed: 351549895

# Time:  O(n * 4^n)
# Space: O(1)

# iterative solution

class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        result = [""]
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result.extend([result[i % n] for i in xrange(n, m*n)])
            for i in xrange(m*n):
                result[i] = choices[i//n] + result[i]
        return result