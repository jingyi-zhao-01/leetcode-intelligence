# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rearrange-array-elements-by-sign
# source_path: LeetCode-Solutions-master/Python/rearrange-array-elements-by-sign.py
# solution_class: Solution2
# submission_id: e171617d8c23806dd34a7dae0d92d095f5967b15
# seed: 3185737103

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution2(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def pos():
            for x in nums:
                if x > 0:
                    yield x
        
        def neg():
            for x in nums:
                if x < 0:
                    yield x
        
        gen_pos = pos()
        gen_neg = neg()
        return [next(gen_pos) if i%2 == 0 else next(gen_neg)  for i in xrange(len(nums))]