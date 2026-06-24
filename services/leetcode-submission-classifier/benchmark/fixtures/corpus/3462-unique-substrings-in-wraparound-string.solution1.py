# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-substrings-in-wraparound-string
# source_path: LeetCode-Solutions-master/Python/unique-substrings-in-wraparound-string.py
# solution_class: Solution
# submission_id: 6bc4e33d82e9dde3e84d8212e0918a772c9576b8
# seed: 2740137169

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        letters = [0] * 26
        result, length = 0, 0
        for i in xrange(len(p)):
            curr = ord(p[i]) - ord('a')
            if i > 0 and ord(p[i-1]) != (curr-1)%26 + ord('a'):
                length = 0
            length += 1
            if length > letters[curr]:
                result += length - letters[curr]
                letters[curr] = length
        return result