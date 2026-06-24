# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsets-ii
# source_path: LeetCode-Solutions-master/Python/subsets-ii.py
# solution_class: Solution2
# submission_id: 84f2525a37555c44e3c44207308034ce67ccd6b8
# seed: 2211147046

# Time:  O(n * 2^n)
# Space: O(1)

class Solution2(object):
    def subsetsWithDup(self, nums):
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
            if cur not in result:
                result.append(cur)
            i += 1

        return result