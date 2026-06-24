# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsets
# source_path: LeetCode-Solutions-master/Python/subsets.py
# solution_class: Solution2
# submission_id: 47d90a4722c57b7abcd1c9091b186ddd92cbf30d
# seed: 651065055

# Time:  O(n * 2^n)
# Space: O(1)

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, count = 0, 1 << len(nums)
        nums.sort()

        while i < count:
            cur = []
            for j in xrange(len(nums)):
                if i & 1 << j:
                    cur.append(nums[j])
            result.append(cur)
            i += 1

        return result