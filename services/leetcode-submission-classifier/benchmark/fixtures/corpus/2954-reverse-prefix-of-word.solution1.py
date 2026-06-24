# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-prefix-of-word
# source_path: LeetCode-Solutions-master/Python/reverse-prefix-of-word.py
# solution_class: Solution
# submission_id: c2f5d90eeabbd72be56f850d5065aa144abcb8fc
# seed: 1247964992

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        i = word.find(ch)
        return word[:i+1][::-1]+word[i+1:]