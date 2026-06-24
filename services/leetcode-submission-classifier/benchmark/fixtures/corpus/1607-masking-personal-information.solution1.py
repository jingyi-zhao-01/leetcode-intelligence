# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: masking-personal-information
# source_path: LeetCode-Solutions-master/Python/masking-personal-information.py
# solution_class: Solution
# submission_id: 8d89c2ba877ccdb9a45a2e97058841e51ecbabb1
# seed: 3585647837

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            first, after = S.split('@')
            return "{}*****{}@{}".format(first[0], first[-1], after).lower()

        digits = filter(lambda x: x.isdigit(), S)
        local = "***-***-{}".format(digits[-4:])
        if len(digits) == 10:
            return local
        return "+{}-{}".format('*' * (len(digits) - 10), local)