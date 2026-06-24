# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-characters-by-frequency
# source_path: LeetCode-Solutions-master/Python/sort-characters-by-frequency.py
# solution_class: Solution
# submission_id: c11736f8a4e48399ff660085a0809da6bad94967
# seed: 2614219607

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1

        counts = [""] * (len(s)+1)
        for c in freq:
            counts[freq[c]] += c

        result = ""
        for count in reversed(xrange(len(counts)-1)):
            for c in counts[count]:
                result += c * count

        return result