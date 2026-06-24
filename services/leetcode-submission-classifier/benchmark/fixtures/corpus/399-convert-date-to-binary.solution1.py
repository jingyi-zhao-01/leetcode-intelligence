# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-date-to-binary
# source_path: LeetCode-Solutions-master/Python/convert-date-to-binary.py
# solution_class: Solution
# submission_id: 441d5620aee6ec8c5f9876a16253e2498201692b
# seed: 1526256692

# Time:  O(1)
# Space: O(1)

# string

class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        return "-".join(map(lambda x: bin(int(x))[2:], date.split('-')))