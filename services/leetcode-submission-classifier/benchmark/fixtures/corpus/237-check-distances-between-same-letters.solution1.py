# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-distances-between-same-letters
# source_path: LeetCode-Solutions-master/Python/check-distances-between-same-letters.py
# solution_class: Solution
# submission_id: 57ef71c45b45046701f87ca9897587b79c5a7c3f
# seed: 743773282

# Time:  O(n)
# Space: O(1)

# hash table

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        for i in xrange(len(s)):
            if i+distance[ord(s[i])-ord('a')]+1 >= len(s) or s[i+distance[ord(s[i])-ord('a')]+1] != s[i]:
                return False
            distance[ord(s[i])-ord('a')] = -1
        return True