# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: implement-strstr
# source_path: LeetCode-Solutions-master/Python/implement-strstr.py
# solution_class: Solution2
# submission_id: 42602a95683d5accada25f712855eedfb8239753
# seed: 3637061766

# Time:  O(n + k)
# Space: O(k)

class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1