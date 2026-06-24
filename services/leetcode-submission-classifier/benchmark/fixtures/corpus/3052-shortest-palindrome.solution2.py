# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-palindrome
# source_path: LeetCode-Solutions-master/Python/shortest-palindrome.py
# solution_class: Solution2
# submission_id: f461fc47ad6a32426c9dc1218a0d5138e8fd2627
# seed: 780691567

# Time:  O(n)
# Space: O(n)

# optimized from Solution2

class Solution2(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j > -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        if not s:
            return s

        A = s + s[::-1]
        prefix = getPrefix(A)
        i = prefix[-1]
        while i >= len(s):
            i = prefix[i]
        return s[i+1:][::-1] + s