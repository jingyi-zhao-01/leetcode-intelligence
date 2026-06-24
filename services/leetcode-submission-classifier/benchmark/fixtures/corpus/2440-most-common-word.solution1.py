# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-common-word
# source_path: LeetCode-Solutions-master/Python/most-common-word.py
# solution_class: Solution
# submission_id: 56620790d13f63285565ea1e400aaf1d8b78180e
# seed: 523183578

# Time:  O(m + n), m is the size of banned, n is the size of paragraph
# Space: O(m + n)

import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lookup = set(banned)
        counts = collections.Counter(word.strip("!?',.")
                                     for word in paragraph.lower().split())

        result = ''
        for word in counts:
            if (not result or counts[word] > counts[result]) and \
               word not in lookup:
                result = word
        return result