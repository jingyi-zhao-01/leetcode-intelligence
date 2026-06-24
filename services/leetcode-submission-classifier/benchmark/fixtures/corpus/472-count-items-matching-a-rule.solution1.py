# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-items-matching-a-rule
# source_path: LeetCode-Solutions-master/Python/count-items-matching-a-rule.py
# solution_class: Solution
# submission_id: 9de115a1b3b881e931f6a604265576a4d2d99149
# seed: 746150884

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        rule = {"type":0, "color":1, "name":2}
        return sum(item[rule[ruleKey]] == ruleValue for item in items)