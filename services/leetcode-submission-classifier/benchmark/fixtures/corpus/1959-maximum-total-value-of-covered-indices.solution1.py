# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-value-of-covered-indices
# source_path: LeetCode-Solutions-master/Python/maximum-total-value-of-covered-indices.py
# solution_class: Solution
# submission_id: 2ada54a4e4bbce15047414d0a509e11c244c6c05
# seed: 4085075066

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxTotal(self, nums, s):
        """
        :type nums: List[int]
        :type s: str
        :rtype: int
        """
        result = i = 0
        while i < len(nums):
            if s[i] == '0':
                i += 1
                continue
            result += nums[i-1] if i-1 >= 0 else 0
            mn = nums[i-1] if i-1 >= 0 else 0
            j = i
            while j < len(s) and s[j] == '1':
                result += nums[j]
                mn = min(mn, nums[j])
                j += 1
            result -= mn
            i = j
        return result