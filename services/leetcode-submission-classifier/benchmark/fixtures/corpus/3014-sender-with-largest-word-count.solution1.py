# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sender-with-largest-word-count
# source_path: LeetCode-Solutions-master/Python/sender-with-largest-word-count.py
# solution_class: Solution
# submission_id: 53e6b8ad5f09dc618e79bcc61f8750c196459990
# seed: 2384304007

# Time:  O(n * l)
# Space: O(n)

import collections
import itertools


# freq table

class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        cnt = collections.Counter()
        for m, s in itertools.izip(messages, senders):
            cnt[s] += m.count(' ')+1
        return max((k for k in cnt.iterkeys()), key=lambda x: (cnt[x], x))