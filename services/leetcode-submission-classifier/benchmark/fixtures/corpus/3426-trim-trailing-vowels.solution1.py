# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trim-trailing-vowels
# source_path: LeetCode-Solutions-master/Python/trim-trailing-vowels.py
# solution_class: Solution
# submission_id: c3711ea87c9df3d3c1f93fbcfb6a09308d365361
# seed: 3938499521

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = "aeiou"
        def f(x):
            return 1<<(ord(x)-ord('a'))

        mask = reduce(lambda accu, x: accu|x, map(f, VOWELS), 0)
        i = next((i for i in reversed(xrange(len(s))) if not f(s[i])&mask), -1)
        return s[:i+1]