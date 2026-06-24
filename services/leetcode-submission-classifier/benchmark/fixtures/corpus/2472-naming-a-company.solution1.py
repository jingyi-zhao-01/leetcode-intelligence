# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: naming-a-company
# source_path: LeetCode-Solutions-master/Python/naming-a-company.py
# solution_class: Solution
# submission_id: 07700ad85ca1be959a4e49b56d3bd3e923a1c4fb
# seed: 207255526

# Time:  O(26 * n * l)
# Space: O(n * l)

# hash table, math

class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        lookup = [set() for _ in xrange(26)]
        for x in ideas:
            lookup[ord(x[0])-ord('a')].add(x[1:])
        result = 0
        for i in xrange(len(lookup)):
            for j in xrange(i+1, len(lookup)):
                common = len(lookup[i]&lookup[j])
                result += (len(lookup[i])-common)*(len(lookup[j])-common)
        return result*2