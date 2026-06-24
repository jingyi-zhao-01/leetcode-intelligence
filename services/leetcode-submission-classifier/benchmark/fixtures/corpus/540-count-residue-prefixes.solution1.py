# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-residue-prefixes
# source_path: LeetCode-Solutions-master/Python/count-residue-prefixes.py
# solution_class: Solution
# submission_id: 87280ef157da97f08085f5701ecb4c3e510bf680
# seed: 4018084416

# Time:  O(n + 26)
# Space: O(26)

# hash table

class Solution(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = distinct = 0
        lookup = [False]*26
        for i, x in enumerate(s):
            if not lookup[ord(x)-ord('a')]:
                distinct += 1
                if distinct >= 3:
                    break
            lookup[ord(x)-ord('a')] = True
            if distinct == (i+1)%3:
                result += 1
        return result