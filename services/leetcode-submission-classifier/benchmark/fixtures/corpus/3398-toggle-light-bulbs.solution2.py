# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: toggle-light-bulbs
# source_path: LeetCode-Solutions-master/Python/toggle-light-bulbs.py
# solution_class: Solution2
# submission_id: a26e00c409253ff00cc06b388a36bdee5157ea67
# seed: 2662788379

# Time:  O(n + r)
# Space: O(r)

# freq table, counting sort

class Solution2(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        cnt = collections.defaultdict(int)
        for x in bulbs:
            cnt[x] ^= 1
        return sorted(k for k, v in cnt.iteritems() if v)