# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-a-string-with-characters-that-have-odd-counts
# source_path: LeetCode-Solutions-master/Python/generate-a-string-with-characters-that-have-odd-counts.py
# solution_class: Solution
# submission_id: c9ea310af3374ab1984cfa8ccdbb5ced8cc69263
# seed: 558920071

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ['a']*(n-1)
        result.append('a' if n%2 else 'b')
        return "".join(result)