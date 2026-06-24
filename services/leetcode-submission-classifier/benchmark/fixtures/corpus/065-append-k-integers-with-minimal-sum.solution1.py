# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: append-k-integers-with-minimal-sum
# source_path: LeetCode-Solutions-master/Python/append-k-integers-with-minimal-sum.py
# solution_class: Solution
# submission_id: f08c54208de726f48143e7587f017b152d3ffc59
# seed: 3507149936

# Time:  O(nlogn)
# Space: O(n)

# greedy

class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = k*(k+1)//2
        curr = k+1
        for x in sorted(set(nums)):
            if x < curr:
                result += curr-x
                curr += 1
        return result