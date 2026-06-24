# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-valid-subarrays
# source_path: LeetCode-Solutions-master/Python/number-of-valid-subarrays.py
# solution_class: Solution
# submission_id: b0f071eb635eb7327be99b8862281af0d3629857
# seed: 3647573824

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        s = []
        for num in nums:
            while s and s[-1] > num:
                s.pop()
            s.append(num)
            result += len(s)
        return result