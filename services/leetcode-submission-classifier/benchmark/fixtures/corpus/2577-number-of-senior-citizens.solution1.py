# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-senior-citizens
# source_path: LeetCode-Solutions-master/Python/number-of-senior-citizens.py
# solution_class: Solution
# submission_id: 8dd30cfa13a57837d0062352358001f5761bbb28
# seed: 1419350979

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        return sum(x[-4:-2] > "60" for x in details)