# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-digits
# source_path: LeetCode-Solutions-master/Python/add-digits.py
# solution_class: Solution
# submission_id: e2c54b3ee4dbebaee09f3dd75742d86493356bbc
# seed: 3513776608

# Time:  O(1)
# Space: O(1)

class Solution(object):
    """
    :type num: int
    :rtype: int
    """
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0