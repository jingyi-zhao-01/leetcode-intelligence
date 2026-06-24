# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: password-strength
# source_path: LeetCode-Solutions-master/Python/password-strength.py
# solution_class: Solution
# submission_id: f001f2a6828efb160ddb1ca6292636e5d1bc100b
# seed: 232960773

# Time:  O(n)
# Space: O(1)

# string, hash table

class Solution(object):
    def passwordStrength(self, password):
        """
        :type password: str
        :rtype: int
        """
        return sum(1 if x.islower() else 2 if x.isupper() else 3 if x.isdigit() else 5 for x in set(password))