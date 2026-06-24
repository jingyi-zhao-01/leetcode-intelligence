# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: group-anagrams
# source_path: LeetCode-Solutions-master/Python/group-anagrams.py
# solution_class: Solution
# submission_id: befd135d07fabdd7a360871460ba5755e0fb59bb
# seed: 1716154676

# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)

import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map, result = collections.defaultdict(list), []
        for s in strs:
            sorted_str = ("").join(sorted(s))
            anagrams_map[sorted_str].append(s)
        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)
        return result