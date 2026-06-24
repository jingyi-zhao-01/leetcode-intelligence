# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: letter-combinations-of-a-phone-number
# source_path: LeetCode-Solutions-master/Python/letter-combinations-of-a-phone-number.py
# solution_class: Solution
# submission_id: 55ba24594534a458a43eeff7638e511b7375e72a
# seed: 1831306390

# Time:  O(n * 4^n)
# Space: O(1)

# iterative solution

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        total = 1
        for digit in digits:
            total *= len(lookup[int(digit)])
        result = []
        for i in xrange(total):
            base, curr = total, []
            for digit in digits:
                choices = lookup[int(digit)]
                base //= len(choices)
                curr.append(choices[(i//base)%len(choices)])
            result.append("".join(curr))
        return result