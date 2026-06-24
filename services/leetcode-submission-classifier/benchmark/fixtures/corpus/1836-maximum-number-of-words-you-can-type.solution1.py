# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-words-you-can-type
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-words-you-can-type.py
# solution_class: Solution
# submission_id: a737696f0ad7d65a3fad2f8bf81838f9780c59bd
# seed: 1432117540

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        lookup = set(brokenLetters)
        result, broken = 0, False
        for c in text:
            if c == ' ':
                result += int(broken == False)
                broken = False
            elif c in lookup:
                broken = True
        return result + int(broken == False)