# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: majority-frequency-characters
# source_path: LeetCode-Solutions-master/Python/majority-frequency-characters.py
# solution_class: Solution
# submission_id: eda4cb30b97968b6c849520b9108b9f504aeb635
# seed: 2009063244

# Time:  O(n + 26)
# Space: O(26)

import collections


# freq table

class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = collections.defaultdict(int)
        for x in s:
            cnt[x] += 1
        cnt2 = collections.defaultdict(list)
        for x, c in cnt.iteritems():
            cnt2[c].append(x)
        k = max(cnt2.iterkeys(), key=lambda x: (len(cnt2[x]), x))
        return "".join(cnt2[k])