# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: decode-the-message
# source_path: LeetCode-Solutions-master/Python/decode-the-message.py
# solution_class: Solution
# submission_id: 8d4ae32e50975fcf2922112cc01acfa93a058b74
# seed: 2622218670

# Time:  O(n + m)
# Space: O(1)

import itertools


# string, hash table

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        f = lambda x: ord(x)-ord('a')
        lookup = [-1]*26
        i = 0
        for x in itertools.imap(f, key):
            if x < 0 or lookup[x] != -1:
                continue
            lookup[x] = i
            i += 1
        return "".join(itertools.imap(lambda x: chr(ord('a')+x), (lookup[x] if x >= 0 else x for x in itertools.imap(f, message))))