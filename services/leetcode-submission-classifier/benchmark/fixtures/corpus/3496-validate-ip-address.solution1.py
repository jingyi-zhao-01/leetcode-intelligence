# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: validate-ip-address
# source_path: LeetCode-Solutions-master/Python/validate-ip-address.py
# solution_class: Solution
# submission_id: 8ba0f886ba2e55430789e8e57927bbc2198a79cc
# seed: 2806285212

# Time:  O(1)
# Space: O(1)

import string

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        blocks = IP.split('.')
        if len(blocks) == 4:
            for i in xrange(len(blocks)):
                if not blocks[i].isdigit() or not 0 <= int(blocks[i]) < 256 or \
                   (blocks[i][0] == '0' and len(blocks[i]) > 1):
                    return "Neither"
            return "IPv4"

        blocks = IP.split(':')
        if len(blocks) == 8:
            for i in xrange(len(blocks)):
                if not (1 <= len(blocks[i]) <= 4) or \
                   not all(c in string.hexdigits for c in blocks[i]):
                    return "Neither"
            return "IPv6"
        return "Neither"