# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-unique-character-in-a-string
# source_path: LeetCode-Solutions-master/Python/first-unique-character-in-a-string.py
# solution_class: Solution
# submission_id: 84f7525ad1c543551b59f5350675c44604cd4ddc
# seed: 548705529

# Time:  O(n)
# Space: O(n)

from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = defaultdict(int)
        candidtates = set()
        for i, c in enumerate(s):
            if lookup[c]:
                candidtates.discard(lookup[c])
            else:
                lookup[c] = i+1
                candidtates.add(i+1)

        return min(candidtates)-1 if candidtates else -1