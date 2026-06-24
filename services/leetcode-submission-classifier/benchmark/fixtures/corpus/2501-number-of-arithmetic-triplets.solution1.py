# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-arithmetic-triplets
# source_path: LeetCode-Solutions-master/Python/number-of-arithmetic-triplets.py
# solution_class: Solution
# submission_id: 29205ce924e3f89bc5e2ba9e8acfd979b7241454
# seed: 3239253257

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        lookup = set(nums)
        return sum((x-diff in lookup) and (x-2*diff in lookup) for x in nums)