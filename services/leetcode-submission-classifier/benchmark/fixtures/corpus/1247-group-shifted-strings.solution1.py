# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: group-shifted-strings
# source_path: LeetCode-Solutions-master/Python/group-shifted-strings.py
# solution_class: Solution
# submission_id: f6b31a41cc5784c1d8f0dc27b24d27cf692d0b78
# seed: 361966290

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        groups = collections.defaultdict(list)
        for s in strings:  # Grouping.
            groups[self.hashStr(s)].append(s)

        result = []
        for key, val in groups.iteritems():
            result.append(sorted(val))

        return result

    def hashStr(self, s):
        base = ord(s[0])
        hashcode = ""
        for i in xrange(len(s)):
            if ord(s[i]) - base >= 0:
                hashcode += unichr(ord('a') + ord(s[i]) - base)
            else:
                hashcode += unichr(ord('a') + ord(s[i]) - base + 26)
        return hashcode