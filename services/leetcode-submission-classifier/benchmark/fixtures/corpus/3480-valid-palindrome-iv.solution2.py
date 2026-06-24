# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-palindrome-iv
# source_path: LeetCode-Solutions-master/Python/valid-palindrome-iv.py
# solution_class: Solution2
# submission_id: 255fe7c0ff3e9d45489a8d7092aac38bd76cc415
# seed: 378334814

# Time:  O(n)
# Space: O(1)

# string, two pointers

class Solution2(object):
    def makePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt = 0
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                cnt += 1
                if cnt > 2:
                    return False
            left += 1
            right -= 1
        return True