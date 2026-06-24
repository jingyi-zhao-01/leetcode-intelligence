# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-close-characters
# source_path: LeetCode-Solutions-master/Python/merge-close-characters.py
# solution_class: Solution
# submission_id: 8dc830db158714d9e5cfc948802979f91ea78f9c
# seed: 3957393318

# Time:  O(n + 26)
# Space: O(26)

# simulation, hash table

class Solution(object):
    def mergeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        lookup = [-1]*26
        for x in s:
            if lookup[ord(x)-ord('a')] != -1 and len(result)-lookup[ord(x)-ord('a')] <= k:
                continue
            lookup[ord(x)-ord('a')] = len(result)
            result.append(x)
        return "".join(result)