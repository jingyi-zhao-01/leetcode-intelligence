# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-make-elements-in-array-distinct
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-make-elements-in-array-distinct.py
# solution_class: Solution
# submission_id: 306a15020d8aece5923516e931fc4da413e2435c
# seed: 1976320146

# Time:  O(n + r)
# Space: O(r)

# freq table

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b

        mx = max(nums)
        cnt = [0]*mx
        for i in reversed(xrange(len(nums))):
            cnt[nums[i]-1] += 1
            if cnt[nums[i]-1] == 2:
                return ceil_divide(i+1, 3)
        return 0