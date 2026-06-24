# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-number
# source_path: LeetCode-Solutions-master/Python/palindrome-number.py
# solution_class: Solution
# submission_id: bf40bc3844ef1609abf43d497720be014e99ac1c
# seed: 385707663

# Time:  O(1)
# Space: O(1)

class Solution(object):
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return x == reverse