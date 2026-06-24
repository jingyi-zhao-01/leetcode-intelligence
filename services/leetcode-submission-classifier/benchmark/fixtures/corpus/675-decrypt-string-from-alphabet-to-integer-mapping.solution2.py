# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decrypt-string-from-alphabet-to-integer-mapping
# source_path: LeetCode-Solutions-master/Python/decrypt-string-from-alphabet-to-integer-mapping.py
# solution_class: Solution2
# submission_id: be9cf35cdc68f8e81e4681ee983e551724f88563
# seed: 3277858353

# Time:  O(n)
# Space: O(1)

# forward solution

class Solution2(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        i = len(s)-1
        result = []
        while i >= 0:
            if s[i] == '#':
                result.append(alpha(s[i-2:i]))
                i -= 3
            else:
                result.append(alpha(s[i]))
                i -= 1
        return "".join(reversed(result))