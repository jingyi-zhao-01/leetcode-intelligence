# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: defanging-an-ip-address
# source_path: LeetCode-Solutions-master/Python/defanging-an-ip-address.py
# solution_class: Solution
# submission_id: 4926eeeb20618425cc1a238030a38548477165bf
# seed: 2519227548

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = []
        for c in address:
            if c == '.':
                result.append("[.]")
            else:
                result.append(c)
        return "".join(result)