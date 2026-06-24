# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-integers-by-binary-reflection
# source_path: LeetCode-Solutions-master/Python/sort-integers-by-binary-reflection.py
# solution_class: Solution
# submission_id: b5aea8fdee50fa0faef87e290cfc44dec488b85f
# seed: 2964129850

# Time:  O(nlogr + nlogn)
# Space: O(n)

# sort, bitmasks

class Solution(object):
    def sortByReflection(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def reverse(x):
            result = 0
            while x:
                result = (result<<1)|(x&1)
                x >>= 1
            return result

        return [x for _, x in sorted((reverse(x), x) for x in nums)]