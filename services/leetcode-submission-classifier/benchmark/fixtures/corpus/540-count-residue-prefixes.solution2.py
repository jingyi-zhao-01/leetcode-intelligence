# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-residue-prefixes
# source_path: LeetCode-Solutions-master/Python/count-residue-prefixes.py
# solution_class: Solution2
# submission_id: 3424ca79a37d290e428a1341c093fae3689588c5
# seed: 899253810

# Time:  O(n + 26)
# Space: O(26)

# hash table

class Solution2(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        lookup = set()
        for i, x in enumerate(s):
            lookup.add(x)
            if len(lookup) >= 3:
                break
            if len(lookup) == (i+1)%3:
                result += 1
        return result