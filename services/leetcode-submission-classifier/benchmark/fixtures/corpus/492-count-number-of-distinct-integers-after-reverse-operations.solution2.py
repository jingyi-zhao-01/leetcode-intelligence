# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-distinct-integers-after-reverse-operations
# source_path: LeetCode-Solutions-master/Python/count-number-of-distinct-integers-after-reverse-operations.py
# solution_class: Solution2
# submission_id: c4e8c9d98daa7a0b849f81dc8aecf86510dba3ae
# seed: 1057578762

# Time:  O(nlogr), r = max(nums)
# Space: O(n)

# hash table   

class Solution2(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len({y for x in nums for y in (x, int(str(x)[::-1]))})