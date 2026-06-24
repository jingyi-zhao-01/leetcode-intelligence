# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shift-distance-between-two-strings
# source_path: LeetCode-Solutions-master/Python/shift-distance-between-two-strings.py
# solution_class: Solution
# submission_id: 78d7e0c23a1696d552edd96b0c1f6f49e31182d7
# seed: 1556199996

# Time:  O(n + 26)
# Space: O(26)

# prefix sum

class Solution(object):
    def shiftDistance(self, s, t, nextCost, previousCost):
        """
        :type s: str
        :type t: str
        :type nextCost: List[int]
        :type previousCost: List[int]
        :rtype: int
        """
        prefix1 = [0]*(len(nextCost)+1)
        for i in xrange(len(nextCost)):
            prefix1[i+1] = prefix1[i]+nextCost[i]
        prefix2 = [0]*(len(previousCost)+1)
        for i in xrange(len(previousCost)):
            prefix2[i+1] = prefix2[i]+previousCost[i]
        result = 0
        for i in xrange(len(s)):
            if s[i] == t[i]:
                continue
            left = ord(s[i])-ord('a')
            right = ord(t[i])-ord('a')
            if left <= right:
                result += min(prefix1[right]-prefix1[left], prefix2[-1]-(prefix2[right+1]-prefix2[left+1]))
            else:
                result += min(prefix2[left+1]-prefix2[right+1], prefix1[-1]-(prefix1[left]-prefix1[right]))
        return result