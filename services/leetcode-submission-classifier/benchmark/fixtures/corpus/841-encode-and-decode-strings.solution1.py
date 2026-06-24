# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: encode-and-decode-strings
# source_path: LeetCode-Solutions-master/Python/encode-and-decode-strings.py
# solution_class: Solution
# submission_id: 806c8f2ea1442f02e57d91e1bb92658a5b301b9d
# seed: 4107686828

# Time:  O(n)
# Space: O(1)

class Codec(object):

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        encoded_str = ""
        for s in strs:
            encoded_str += "%0*x" % (8, len(s)) + s
        return encoded_str


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i = 0
        strs = []
        while i < len(s):
            l = int(s[i:i+8], 16)
            strs.append(s[i+8:i+8+l])
            i += 8+l
        return strs

