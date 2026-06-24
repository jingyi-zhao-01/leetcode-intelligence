# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-word-abbreviation
# source_path: LeetCode-Solutions-master/Python/valid-word-abbreviation.py
# solution_class: Solution
# submission_id: 0053a63df76e3cc12f2398bed75e4831eea00f71
# seed: 3487296064

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i , digit = 0, 0
        for c in abbr:
            if c.isdigit():
                if digit == 0 and c == '0':
                    return False
                digit *= 10
                digit += int(c)
            else:
                if digit:
                    i += digit
                    digit = 0
                if i >= len(word) or word[i] != c:
                    return False
                i += 1
        if digit:
            i += digit

        return i == len(word)