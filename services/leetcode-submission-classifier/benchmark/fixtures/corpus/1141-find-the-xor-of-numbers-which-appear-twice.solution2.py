# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-xor-of-numbers-which-appear-twice
# source_path: LeetCode-Solutions-master/Python/find-the-xor-of-numbers-which-appear-twice.py
# solution_class: Solution2
# submission_id: 43fa281c12012b560cf8bb07499455a910a6c1f2
# seed: 3562332567

# Time:  O(n)
# Space: O(n)

# hash table

class Solution2(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x^y, (x for x, c in collections.Counter(nums).iteritems() if c == 2), 0)