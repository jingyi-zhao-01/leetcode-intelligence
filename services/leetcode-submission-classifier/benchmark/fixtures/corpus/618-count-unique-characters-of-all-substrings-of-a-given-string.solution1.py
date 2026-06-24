# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-unique-characters-of-all-substrings-of-a-given-string
# source_path: LeetCode-Solutions-master/Python/count-unique-characters-of-all-substrings-of-a-given-string.py
# solution_class: Solution
# submission_id: 2698fbd9148207d54578dc0a919991ed73c00094
# seed: 4261971640

# Time:  O(n)
# Space: O(1)

import string

class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        M = 10**9 + 7
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        result = 0
        for i, c in enumerate(S):
            k, j = index[c]
            result = (result + (i-j) * (j-k)) % M
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            result = (result + (len(S)-j) * (j-k)) % M
        return result