# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: letter-combinations-of-a-phone-number
# source_path: LeetCode-Solutions-master/Python/letter-combinations-of-a-phone-number.py
# solution_class: Solution3
# submission_id: efe5dd56d15d89e5c32aaa63ad502bf57790ee04
# seed: 3506450548

# Time:  O(n * 4^n)
# Space: O(1)

# iterative solution

class Solution3(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def letterCombinationsRecu(result, digits, curr, n):
            if n == len(digits):
                result.append("".join(curr))
                return
            for choice in lookup[int(digits[n])]:
                curr.append(choice)
                letterCombinationsRecu(result, digits, curr, n+1)
                curr.pop()

        if not digits:
            return []
        result = []
        letterCombinationsRecu(result, digits, [], 0)
        return result