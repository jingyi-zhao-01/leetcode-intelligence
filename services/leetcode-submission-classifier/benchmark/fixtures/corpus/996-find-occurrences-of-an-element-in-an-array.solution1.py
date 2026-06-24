# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-occurrences-of-an-element-in-an-array
# source_path: LeetCode-Solutions-master/Python/find-occurrences-of-an-element-in-an-array.py
# solution_class: Solution
# submission_id: 1b079cfe60ab5782761ac181f9a1c513f93993a3
# seed: 2587238980

# Time:  O(n + q)
# Space: O(n)

# array

class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        lookup = [i for i, y in enumerate(nums) if y == x]
        return [lookup[q-1] if q-1 < len(lookup) else -1 for q in queries]