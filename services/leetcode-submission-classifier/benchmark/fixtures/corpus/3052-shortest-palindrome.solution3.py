# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-palindrome
# source_path: LeetCode-Solutions-master/Python/shortest-palindrome.py
# solution_class: Solution3
# submission_id: 1ed17f3faf3f3b2172545d18b82779405252b69a
# seed: 2411660589

# Time:  O(n)
# Space: O(n)

# optimized from Solution2

class Solution3(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preProcess(s):
            if not s:
                return ['^', '$']
            string = ['^']
            for c in s:
                string +=  ['#', c]
            string += ['#', '$']
            return string

        string = preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        for i in xrange(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len = 0
        for i in xrange(1, len(string) - 1):
            if i - palindrome[i] == 1:
                max_len = palindrome[i]
        return s[len(s)-1:max_len-1:-1] + s