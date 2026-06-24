# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-if-string-halves-are-alike
# source_path: LeetCode-Solutions-master/Python/determine-if-string-halves-are-alike.py
# solution_class: Solution
# submission_id: eea87a53f4684750522c360e07b025905e34df68
# seed: 3326998347

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set("aeiouAEIOU")
        cnt1 = cnt2 = 0
        left, right = 0, len(s)-1
        while left < right:
            cnt1 += s[left] in vowels
            cnt2 += s[right] in vowels
            left += 1
            right -= 1
        return cnt1 == cnt2