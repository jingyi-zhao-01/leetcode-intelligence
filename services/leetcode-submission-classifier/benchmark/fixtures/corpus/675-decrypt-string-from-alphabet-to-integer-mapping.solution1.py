# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decrypt-string-from-alphabet-to-integer-mapping
# source_path: LeetCode-Solutions-master/Python/decrypt-string-from-alphabet-to-integer-mapping.py
# solution_class: Solution
# submission_id: 51e8d5467920546f55da8962c4e99e6dbf6fa60e
# seed: 3635213749

# Time:  O(n)
# Space: O(1)

# forward solution

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        i = 0
        result = []
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                result.append(alpha(s[i:i+2]))
                i += 3
            else:
                result.append(alpha(s[i]))
                i += 1
        return "".join(result)