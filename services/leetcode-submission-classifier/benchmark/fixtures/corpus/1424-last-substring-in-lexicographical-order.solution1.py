# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: last-substring-in-lexicographical-order
# source_path: LeetCode-Solutions-master/Python/last-substring-in-lexicographical-order.py
# solution_class: Solution
# submission_id: 04b0d3839523a229f98c417e76fb58de1f571ce8
# seed: 3828746542

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right, l = 0, 1, 0
        while right+l < len(s):
            if s[left+l] == s[right+l]:
                l += 1
                continue
            if s[left+l] > s[right+l]:
                right += l+1
            else:
                left = max(right, left+l+1)
                right = left+1
            l = 0
        return s[left:]