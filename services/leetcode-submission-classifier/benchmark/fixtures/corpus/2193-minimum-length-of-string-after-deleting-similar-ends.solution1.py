# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-length-of-string-after-deleting-similar-ends
# source_path: LeetCode-Solutions-master/Python/minimum-length-of-string-after-deleting-similar-ends.py
# solution_class: Solution
# submission_id: 3f70b4b31e3797b3180a2ab0faaf215dafb9d0e6
# seed: 437699224

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                break
            c = s[left]
            while left <= right:
                if s[left] != c:
                    break
                left += 1
            while left <= right:
                if s[right] != c:
                    break
                right -= 1
        return right-left+1