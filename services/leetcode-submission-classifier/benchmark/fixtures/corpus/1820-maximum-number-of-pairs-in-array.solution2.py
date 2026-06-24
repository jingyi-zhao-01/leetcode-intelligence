# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-pairs-in-array
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-pairs-in-array.py
# solution_class: Solution2
# submission_id: 24561f4235f1c9ce9c30e7439ed8f91ce0845afc
# seed: 3559712596

# Time:  O(n)
# Space: O(r), r = max(nums)

# freq table

class Solution2(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = collections.Counter(nums)
        pair_cnt = sum(x//2 for x in cnt.itervalues())
        return [pair_cnt, len(nums)-2*pair_cnt]