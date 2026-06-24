# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: strong-password-checker-ii
# source_path: LeetCode-Solutions-master/Python/strong-password-checker-ii.py
# solution_class: Solution
# submission_id: fd92dfac038a5e42ca0e4ae79745114ab153bd58
# seed: 1233057194

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        SPECIAL = set("!@#$%^&*()-+")
        return (len(password) >= 8 and
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in SPECIAL for c in password) and
                all(password[i] != password[i+1] for i in xrange(len(password)-1)))