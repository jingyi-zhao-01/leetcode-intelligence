# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decrypt-string-from-alphabet-to-integer-mapping
# source_path: LeetCode-Solutions-master/Python/decrypt-string-from-alphabet-to-integer-mapping.py
# solution_class: Solution3
# submission_id: e2faa6c108e04ec855ffad1a5a0786c41378ad1c
# seed: 2658090895

# Time:  O(n)
# Space: O(1)

# forward solution

class Solution3(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        return "".join(alpha(i[:2]) for i in re.findall(r"\d\d#|\d", s))