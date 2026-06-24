# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-letter-to-appear-twice
# source_path: LeetCode-Solutions-master/Python/first-letter-to-appear-twice.py
# solution_class: Solution
# submission_id: e0837117f27d02bdd1c3cde93ca9dea3976ab2ab
# seed: 3322230

# Time:  O(n)
# Space: O(1)

# hash table

class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        lookup = set()
        for c in s:
            if c in lookup:
                break
            lookup.add(c)
        return c